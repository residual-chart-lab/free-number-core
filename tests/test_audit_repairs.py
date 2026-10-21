"""Regression conditions from Astra's three PR13 runtime findings."""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'runtime'))
import json
import os
import subprocess
import tempfile
import unittest
from dataclasses import replace
from fractions import Fraction as Q

from free_numbers import *
from free_numbers.algebra import canonical, integer_text, parse_integer_text
from free_numbers.checkpoint import dumps,loads,CheckpointLimits


def scope():
    return Scope('astra-audit','bounded-expression','exact-response')


def chain(count):
    one = constant(ONE)
    root = one
    for _ in range(count-1):
        root = root+one
    return root


class CheckpointBoundaryTests(unittest.TestCase):
    def test_reference_default_boundary_and_explicit_extension(self):
        vault = Vault()
        root = constant(ONE)
        for i in range(10001):
            vault.register(str(i),0,(0,0),'origin')
            if i+1 in (9999,10000):
                raw,h = dumps((root,),vault)
                roots,restored = loads(raw,h)
                self.assertEqual(len(restored._records()),i+1)
                self.assertEqual(dumps(roots,restored),(raw,h))
        with self.assertRaises(ValueError):
            dumps((root,),vault)
        limits = CheckpointLimits(max_references=10001)
        raw,h = dumps((root,),vault,limits)
        roots,restored = loads(raw,h,limits)
        self.assertEqual(len(restored._records()),10001)
        self.assertEqual(dumps(roots,restored,limits),(raw,h))
        with self.assertRaises(ValueError):
            loads(raw,h)  # A smaller reader budget is an explicit rejection.

    def test_node_boundary_is_shared_by_writer_and_reader(self):
        limits = CheckpointLimits(max_nodes=16)
        for count in (15,16):
            root = chain(count)
            raw,h = dumps((root,),Vault(),limits)
            roots,v = loads(raw,h,limits)
            self.assertEqual(roots[0].digest,root.digest)
        with self.assertRaises(ValueError):
            dumps((chain(17),),Vault(),limits)
        raw,h = dumps((chain(17),),Vault())
        with self.assertRaises(ValueError):
            loads(raw,h,limits)

    def test_byte_boundary_is_shared_by_writer_and_reader(self):
        root,vault = constant(ONE),Vault()
        raw,h = dumps((root,),vault)
        for size in (len(raw),len(raw)+1):
            limits = CheckpointLimits(max_bytes=size)
            self.assertEqual(dumps((root,),vault,limits),(raw,h))
            self.assertEqual(loads(raw,h,limits)[0][0].digest,root.digest)
        limits = CheckpointLimits(max_bytes=len(raw)-1)
        with self.assertRaises(ValueError):
            dumps((root,),vault,limits)
        with self.assertRaises(ValueError):
            loads(raw,h,limits)

    def test_checkpoint_budgets_are_explicit_positive_integers(self):
        for limits in (dict(max_nodes=0),dict(max_references=-1),dict(max_bytes=True)):
            with self.assertRaises(ValueError):
                CheckpointLimits(**limits)


class LongExpressionTests(unittest.TestCase):
    def test_1201_circuit_nodes_evaluate_and_roundtrip(self):
        root = chain(1201)
        query = Query(root,scope())
        proof = evaluate(query,Vault())
        self.assertEqual(proof.value,(1201,0,0,0))
        self.assertTrue(verify_certificate(query,Vault(),proof))
        raw,h = dumps((root,),Vault())
        (restored,),vault = loads(raw,h)
        self.assertEqual(evaluate(Query(restored,scope()),vault),proof)

    def test_1201_tensor_sum_nodes_evaluate_and_roundtrip(self):
        unit = block(1,(((0,),1),))
        root = unit
        for _ in range(1200):
            root = root+unit
        expression = read(root)
        proof = evaluate(Query(expression,scope()),Vault())
        self.assertEqual(proof.value,(0,1201,0,0))
        raw,h = dumps((expression,),Vault())
        (restored,),vault = loads(raw,h)
        self.assertEqual(evaluate(Query(restored,scope()),vault),proof)

    def test_1201_ordered_tensor_factors_do_not_use_python_recursion(self):
        unit = block(1,(((0,),1),))
        root = unit
        for _ in range(1200):
            root = root.then(unit)
        expression = read(root)
        self.assertEqual(evaluate(Query(expression,scope()),Vault()).value,BASIS[1])
        raw,h = dumps((expression,),Vault())
        (restored,),vault = loads(raw,h)
        self.assertEqual(evaluate(Query(restored,scope()),vault).value,BASIS[1])

    def test_deliberately_small_budgets_remain_undetermined_or_reject(self):
        root = chain(1201)
        self.assertEqual(evaluate(Query(root,scope()),Vault(),Policy(max_nodes=1000)).status,
                         'UNDETERMINED_PROOF_BUDGET')
        with self.assertRaises(ValueError):
            dumps((root,),Vault(),CheckpointLimits(max_nodes=1000))


class ExactIntegerTests(unittest.TestCase):
    def test_sixteen_nodes_compute_a_32769_bit_coefficient(self):
        root = constant((2,0,0,0))
        for _ in range(15):
            root = root*root
        query = Query(root,scope())
        p = plan(query,Vault())
        self.assertEqual(p.status,'AVAILABLE')
        self.assertEqual(p.coefficients[0][1][0].numerator.bit_length(),32769)
        proof = evaluate(query,Vault())
        self.assertEqual(proof.value,(1<<32768,0,0,0))
        self.assertEqual(len(proof.digest),64)
        raw,h = dumps((root,),Vault())
        (restored,),vault = loads(raw,h)
        self.assertEqual(evaluate(Query(restored,scope()),vault),proof)

    def test_large_rational_exact_read_and_separate_process_restore(self):
        vault = Vault()
        value = Q((1<<40000)+7,(1<<33000)+9)
        direction = matrix_block(((1,0,0),(0,-1,0),(0,0,0)))
        root = retained(vault,'large',value,(value-1,value+1),'exact-origin',block(2,()),direction)
        vault.register('unused-negative',-value,(-value-1,-value+1),'retained-unused')
        obs = Observation(2,(Channel(((1,0,0),)),))
        expression = read(root,obs)
        proof = evaluate(Query(expression,scope()),vault)
        self.assertEqual(proof.value,(0,-2*value,0,0))
        raw,h = dumps((expression,),vault)
        program = '''
import sys,json
from fractions import Fraction as Q
from pathlib import Path
from free_numbers import *
from free_numbers.checkpoint import loads,dumps
payload=Path(sys.argv[1]).read_bytes()
(root,),vault=loads(payload,sys.argv[2])
value=Q((1<<40000)+7,(1<<33000)+9)
result=evaluate(Query(root,Scope('astra-audit','bounded-expression','exact-response')),vault)
assert result.value==(0,-2*value,0,0)
assert len(vault._records())==2
assert dumps((root,),vault)==(payload,sys.argv[2])
print(json.dumps(dict(passed=True,integer_limit=getattr(sys,'get_int_max_str_digits',lambda:None)())))
'''
        before = getattr(sys,'get_int_max_str_digits',lambda:None)()
        env = {**os.environ,'PYTHONPATH':str(ROOT/'runtime')}
        directory = ROOT/'.work/audit-tests'
        directory.mkdir(parents=True,exist_ok=True)
        with tempfile.NamedTemporaryFile(dir=directory,suffix='.json',delete=False) as saved:
            path = Path(saved.name)
            saved.write(raw)
        try:
            result = subprocess.run([sys.executable,'-X','int_max_str_digits=4300','-c',program,str(path),h],
                env=env,text=True,capture_output=True,encoding='utf-8',timeout=60)
        finally:
            path.unlink()
        self.assertEqual(result.returncode,0,result.stderr)
        report = json.loads(result.stdout)
        self.assertTrue(report['passed'])
        if hasattr(sys,'get_int_max_str_digits'):
            self.assertEqual(report['integer_limit'],4300)
        self.assertEqual(getattr(sys,'get_int_max_str_digits',lambda:None)(),before)

    def test_codec_is_canonical_at_the_minimum_digit_limit(self):
        for text in ('','+1','-0','00','01','-01',' 1','1 ','١'):
            with self.assertRaises(ValueError):
                parse_integer_text(text)
        for value in (0,1,-1,1<<32768,-((1<<32768)+3)):
            self.assertEqual(parse_integer_text(integer_text(value)),value)
        values = (Q((1<<32768)+3,(1<<33000)+7),1<<2000,1<<40000)
        expected = canonical(values).hex()
        program = '''
from fractions import Fraction as Q
from free_numbers.algebra import canonical
print(canonical((Q((1<<32768)+3,(1<<33000)+7),1<<2000,1<<40000)).hex())
'''
        env = {**os.environ,'PYTHONPATH':str(ROOT/'runtime')}
        result = subprocess.run([sys.executable,'-X','int_max_str_digits=640','-c',program],
            env=env,text=True,capture_output=True,encoding='utf-8',timeout=60)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(result.stdout.strip(),expected)


if __name__ == '__main__':
    unittest.main()
