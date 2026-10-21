import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'runtime'))
import unittest
from dataclasses import replace
from fractions import Fraction as Q
from itertools import product, combinations
import json
import random
from hashlib import sha256

from free_numbers import *
from free_numbers.algebra import qmul, canonical
from free_numbers.checkpoint import dumps,loads
import oracle

E = tuple(tuple(Q(i==j) for i in range(3)) for j in range(3))
S = matrix_block(((1,0,0),(0,-1,0),(0,0,0)))
T = matrix_block(((0,1,0),(1,0,0),(0,0,0)))
EMPTY = block(2,())


def scope(tag='one'):
    return Scope('same-entry',tag,'declared-response')


def pair():
    vault = Vault()
    a = retained(vault,'s',Q(1,3),(-1,1),'source-A',EMPTY,S)
    b = retained(vault,'t',Q(2,5),(0,1),'source-B',EMPTY,T)
    return vault,a,b


class AlgebraTests(unittest.TestCase):
    def test_registered_component_projection(self):
        for i in range(4):
            expression = constant((Q(2,3),Q(-5,7),Q(11),Q(-13,9)))
            got = evaluate(Query(component(expression,i),scope()),Vault()).value
            self.assertEqual(got,(expression.data[0][i],Q(0),Q(0),Q(0)))

    def test_reversed_order_and_bridge(self):
        a,b = block(1,(((0,),1),)),block(1,(((1,),1),))
        self.assertEqual(evaluate(Query(read(a.then(b)),scope()),Vault()).value,(0,0,0,-1))
        r = read(a.then(b),Observation(2,(Channel((E[2],)),)))
        self.assertEqual(evaluate(Query(r,scope()),Vault()).value,oracle.circuit(r,{}))

    def test_all_small_grade_basis_words_and_masks(self):
        count = 0
        for n in range(1,5):
            for word in product(range(3),repeat=n):
                leaves = [block(1,(((a,),1),)) for a in word]
                joined = leaves[0]
                for a in leaves[1:]:
                    joined = joined.then(a)
                for gaps in product((None,)+E,repeat=n-1):
                    r = read(joined,Observation(n,(Channel(gaps),)))
                    got = evaluate(Query(r,scope()),Vault()).value
                    self.assertEqual(got,oracle.circuit(r,{}))
                    count += 1
        self.assertEqual(count,5655)

    def test_associative_composition_preserves_order(self):
        a,b,c = (block(1,(((i,),1),)) for i in range(3))
        o = Observation(3,(Channel((E[1],E[0])),))
        x,y = read(a.then(b).then(c),o),read(a.then(b.then(c)),o)
        self.assertEqual(evaluate(Query(x,scope()),Vault()).value,evaluate(Query(y,scope()),Vault()).value)
        self.assertNotEqual(a.then(b).digest,b.then(a).digest)

    def test_zero_compression_does_not_delete_residual(self):
        vault,a,b = pair()
        before = a.digest
        m = Meter()
        p = plan(Query(read(a),scope()),vault,meter=m)
        self.assertEqual(p.dependencies,())
        self.assertEqual(evaluate(Query(read(a),scope()),vault,meter=m).value,ZERO)
        self.assertEqual(m.exact_reads,0)
        obs = Observation(2,(Channel((E[0],)),))
        self.assertEqual(plan(Query(read(a,obs),scope('later')),vault).dependencies,('s',))
        self.assertNotEqual(evaluate(Query(read(a,obs),scope('later')),vault).value,ZERO)
        self.assertEqual(a.digest,before)

    def test_interactions_survive_zero_first_derivatives(self):
        vault,a,b = pair()
        r = read(a.then(b),Observation(4,(Channel((E[0],None,E[0])),)))
        p = plan(Query(r,scope('pair')),vault)
        self.assertEqual(p.dependencies,('s','t'))
        self.assertEqual(p.interacting_monomials,(('s','t'),))
        self.assertEqual(evaluate(Query(r,scope('pair')),vault).value,oracle.circuit(r,{'s':Q(1,3),'t':Q(2,5)}))

    def test_repeated_reference_is_a_power(self):
        vault,a,b = pair()
        r = read(a.then(a),Observation(4,(Channel((E[0],None,E[0])),)))
        p = plan(Query(r,scope()),vault)
        self.assertEqual(p.interacting_monomials,(('s','s'),))
        self.assertEqual(evaluate(Query(r,scope()),vault).value,oracle.circuit(r,{'s':Q(1,3)}))

    def test_whole_polynomial_cancellation_avoids_reads(self):
        vault,a,b = pair()
        r = read(a,Observation(2,(Channel((E[0],)),)))
        r = r + constant((-1,0,0,0))*r
        m = Meter()
        self.assertEqual(plan(Query(r,scope()),vault).dependencies,())
        self.assertEqual(evaluate(Query(r,scope()),vault,meter=m).value,ZERO)
        self.assertEqual(m.exact_reads,0)

    def test_all_depth_one_channels_are_blind_to_pair(self):
        vault,a,b = pair()
        for gap in range(3):
            for vector in E:
                gaps = tuple(vector if i==gap else None for i in range(3))
                q = Query(read(a.then(b),Observation(4,(Channel(gaps),))),scope())
                self.assertEqual(plan(q,vault).dependencies,())
                self.assertEqual(evaluate(q,vault).value,ZERO)

    def test_sum_scale_general_probes_and_ordered_circuit(self):
        vault,a,b = pair()
        x = (a + S.scaled(Q(-2,7))).then(b)
        obs = Observation(4,(Channel(((Q(1,2),Q(-1,3),Q(2)),None,E[2]),Q(3,5),BASIS[2],BASIS[1]),))
        r = constant(BASIS[3])*read(x,obs) + read(b,Observation(2,(Channel((E[1],)),)))
        self.assertEqual(evaluate(Query(r,scope()),vault).value,oracle.circuit(r,{'s':Q(1,3),'t':Q(2,5)}))

    def test_long_shared_expression_does_not_expand_tensor(self):
        x = matrix_block(((Q(1,3),0,0),(0,Q(1,3),0),(0,0,Q(1,3))))
        for _ in range(6):
            x = x.then(x)
        self.assertEqual(x.grade,128)
        m = Meter()
        cert = evaluate(Query(read(x),scope()),Vault(),Policy(max_depth=0),m)
        self.assertEqual(cert.value,ONE)
        self.assertLess(m.compiled_tensor_slices,10)
        self.assertGreater(m.compile_cache_hits,0)


class EvaluationTests(unittest.TestCase):
    def test_deterministic_mixed_polynomials_match_dense_oracle_and_bounds(self):
        rng = random.Random(721194)
        for case in range(40):
            vault,a,b = pair()
            base = block(2,(((i,j),Q(rng.randint(-3,3),rng.randint(1,5)))
                            for i in range(3) for j in range(3)))
            x = (a+base).then(b+S.scaled(Q(1,7)))
            gaps = tuple(None if rng.randrange(3)==0 else tuple(Q(rng.randint(-2,2),3) for _ in range(3)) for _ in range(3))
            r = read(x,Observation(4,(Channel(gaps),)))
            r = r*read(a,Observation(2,(Channel((E[case%3],)),))) + r
            exact = oracle.circuit(r,{'s':Q(1,3),'t':Q(2,5)})
            self.assertEqual(evaluate(Query(r,scope()),vault).value,exact)
            offset = tuple(Q(rng.randint(-1,1),5) for _ in range(4))
            target = tuple(v+d for v,d in zip(exact,offset))
            q = Query(r,scope(),'within-l1',target,Q(1,3))
            cert = evaluate(q,vault,Policy(precisions=(4,16,48)))
            self.assertEqual(cert.decision,sum(abs(v-t) for v,t in zip(exact,target))<Q(1,3))
            for stage in cert.stages:
                self.assertTrue(all(lo<=v<=hi for (lo,hi),v in zip(stage.bounds,exact)))

    def test_replacement_judgement_is_scoped_and_preserves_difference(self):
        vault,a,b = pair()
        original = a.digest
        self.assertEqual(assess_replacement(read(a),read(EMPTY),scope(),vault).status,'REPLACEABLE_IN_SCOPE')
        obs = Observation(2,(Channel((E[0],)),))
        self.assertEqual(assess_replacement(read(a,obs),read(EMPTY,obs),scope('later'),vault).status,'NOT_REPLACEABLE_IN_SCOPE')
        unknown = assess_replacement(read(a,obs),read(EMPTY,obs),scope('later'),vault,Policy(max_depth=0))
        self.assertEqual(unknown.status,'UNDETERMINED')
        self.assertEqual(a.digest,original)

    def test_query_selects_only_visible_direction(self):
        vault,a,b = pair()
        r = read(a,Observation(2,(Channel((E[0],)),))) + read(b)
        p = plan(Query(r,scope()),vault)
        self.assertEqual(p.dependencies,('s',))
        m = Meter()
        evaluate(Query(r,scope()),vault,meter=m)
        self.assertEqual(m.exact_reads,1)

    def test_existence_style_predicate_needs_no_exact_value(self):
        vault,a,b = pair()
        q = Query(read(a,Observation(2,(Channel((E[0],)),))),scope(),'within-l1',ZERO,Q(3))
        m = Meter()
        c = evaluate(q,vault,meter=m)
        self.assertTrue(c.decision)
        self.assertEqual(m.refinement_reads,0)
        self.assertEqual(m.exact_reads,0)
        self.assertIsNone(c.value)

    def test_precision_increases_without_changing_observation(self):
        vault,a,b = pair()
        r = read(a,Observation(2,(Channel((E[0],)),)))
        q = Query(r,scope(),'within-l1',(0,Q(-2,3),0,0),Q(1,10**12))
        policy = Policy(max_depth=1,precisions=(4,16,48),exact_fallback=False)
        m = Meter()
        c = evaluate(q,vault,policy,m)
        self.assertTrue(c.decision)
        self.assertEqual(c.stages[-1].bits,48)
        self.assertEqual(m.exact_reads,0)
        for stage in c.stages:
            exact = oracle.circuit(r,{'s':Q(1,3)})
            self.assertTrue(all(lo<=v<=hi for (lo,hi),v in zip(stage.bounds,exact)))

    def test_more_bits_cannot_fix_missing_depth(self):
        vault,a,b = pair()
        q = Query(read(a.then(b),Observation(4,(Channel((E[0],None,E[0])),))),scope())
        for bits in (8,128,1024):
            m = Meter()
            c = evaluate(q,vault,Policy(max_depth=1,precisions=(bits,)),m)
            self.assertEqual(c.status,'UNDETERMINED_DEPTH_BUDGET')
            self.assertEqual(m.exact_reads,0)
        self.assertNotEqual(evaluate(q,vault,Policy(max_depth=2)).value,ZERO)

    def test_strict_threshold_and_exact_fallback(self):
        vault,a,b = pair()
        q = Query(read(a,Observation(2,(Channel((E[0],)),))),scope(),'within-l1',ZERO,Q(2,3))
        c = evaluate(q,vault,Policy(precisions=(8,),exact_fallback=False))
        self.assertIsNone(c.decision)
        c = evaluate(q,vault,Policy(precisions=(8,)))
        self.assertFalse(c.decision)
        self.assertEqual(c.exact_keys,('s',))

    def test_symbolic_budget_failure_is_not_a_zero_witness(self):
        vault,a,b = pair()
        r = read(a,Observation(2,(Channel((E[0],)),)))+read(b,Observation(2,(Channel((E[0],)),)))
        q = Query(r,scope())
        c = evaluate(q,vault,Policy(max_terms=1))
        self.assertEqual(c.status,'UNDETERMINED_PROOF_BUDGET')
        self.assertIsNone(c.value)

    def test_channel_and_graph_budgets_remain_unknown(self):
        vault,a,b = pair()
        obs = Observation(2,(Channel((E[0],)),Channel((E[1],))))
        q = Query(read(a,obs),scope())
        for policy in (Policy(max_nodes=1),Policy(max_channels=1)):
            self.assertEqual(evaluate(q,vault,policy).status,'UNDETERMINED_PROOF_BUDGET')

    def test_certificate_binds_scope_target_policy_and_expression(self):
        vault,a,b = pair()
        q = Query(read(a),scope(),'within-l1',ZERO,Q(1))
        c = evaluate(q,vault)
        self.assertTrue(verify_certificate(q,vault,c))
        for changed in (replace(q,scope=scope('new-flower')),replace(q,tolerance=Q(2)),
                        replace(q,expression=read(b)),replace(q,target=ONE)):
            with self.assertRaises(ValueError):
                verify_certificate(changed,vault,c)
        with self.assertRaises(ValueError):
            verify_certificate(q,vault,replace(c,status='MADE_UP'))
        with self.assertRaises(ValueError):
            verify_certificate(q,vault,c,Policy(max_depth=0))

    def test_plan_and_reference_tampering_rejected(self):
        vault,a,b = pair()
        q = Query(read(a),scope())
        p = plan(q,vault)
        with self.assertRaises(ValueError):
            verify_plan(q,vault,Policy(),replace(p,requested_depth=9))
        forged_ref = replace(a.data[0],origin='someone-else')
        forged = Tensor('retained',2,(forged_ref,),a.children)
        with self.assertRaises(ValueError):
            plan(Query(read(forged),scope()),vault)

    def test_no_envelope_or_key_rebinding(self):
        vault,a,b = pair()
        with self.assertRaises(ValueError):
            vault.register('s',Q(1,2),(-1,1),'source-A')
        with self.assertRaises(ValueError):
            vault.register('u',Q(2),(0,1),'outside')

    def test_small_and_large_residues_follow_response_not_magnitude(self):
        for value in (Q(1,10**20),Q(10**50)):
            vault = Vault()
            a = retained(vault,'r',value,(value-1,value+1),'large-or-small',EMPTY,S)
            m = Meter()
            self.assertEqual(evaluate(Query(read(a),scope()),vault,meter=m).value,ZERO)
            self.assertEqual(m.exact_reads,0)
            q = Query(read(a,Observation(2,(Channel((E[0],)),))),scope('later'))
            self.assertNotEqual(evaluate(q,vault).value,ZERO)


class CheckpointTests(unittest.TestCase):
    def test_roundtrip_preserves_unused_values_and_shared_subgraphs(self):
        vault,a,b = pair()
        first = read(a.then(a))
        later = read(a.then(b),Observation(4,(Channel((E[0],None,E[0])),)))
        before = evaluate(Query(first,scope()),vault)
        raw,h = dumps((first,later),vault)
        (x,y),restored = loads(raw,h)
        self.assertIs(x.data[0].children[0],x.data[0].children[1])
        self.assertEqual(evaluate(Query(x,scope()),restored),before)
        self.assertEqual(evaluate(Query(y,scope('later')),restored),evaluate(Query(later,scope('later')),vault))
        self.assertEqual(dumps((x,y),restored),(raw,h))
        self.assertEqual(len(restored._records()),2)

    def test_untrusted_outer_hash_rejected(self):
        vault,a,b = pair()
        raw,h = dumps((read(a),),vault)
        for payload,expected in ((raw,None),(raw,'0'*64),(raw+b' ',h)):
            with self.assertRaises(ValueError):
                loads(payload,expected)

    def test_internal_changes_rejected_even_with_new_outer_hash(self):
        vault,a,b = pair()
        raw,h = dumps((read(a.then(b)),),vault)
        for mutation in ('origin','order','bound','node-id','unknown-operation'):
            d = json.loads(raw)
            if mutation == 'origin':
                d['retained'][0][3] = 'changed'
            elif mutation == 'bound':
                d['retained'][0][2][0] = {'q':['-2','1']}
            elif mutation == 'order':
                node = next(n for n in d['nodes'] if n['kind']=='concat')
                node['children'].reverse()
            elif mutation == 'node-id':
                d['nodes'][0]['id'] = '0'*64
            else:
                d['nodes'][0]['kind'] = 'python-eval'
            changed = json.dumps(d).encode()
            with self.assertRaises(ValueError):
                loads(changed,sha256(changed).hexdigest())

    def test_scope_certificate_does_not_transfer_after_restore(self):
        vault,a,b = pair()
        root = read(a.then(b))
        q = Query(root,scope())
        c = evaluate(q,vault)
        raw,h = dumps((root,),vault)
        (root2,),v2 = loads(raw,h)
        self.assertTrue(verify_certificate(Query(root2,scope()),v2,c))
        with self.assertRaises(ValueError):
            verify_certificate(Query(root2,scope('upper-flower')),v2,c)

    def test_wrong_types_and_float_inputs_rejected(self):
        with self.assertRaises(TypeError):
            matrix_block(((0.1,0,0),(0,0,0),(0,0,0)))
        with self.assertRaises(ValueError):
            Policy(precisions=(32,16))
        with self.assertRaises(ValueError):
            Observation(2,(Channel(()),))


if __name__ == '__main__':
    unittest.main()
