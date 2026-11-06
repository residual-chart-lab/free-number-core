"""Exact exterior SU(2)-connection / fixed Free Numbers B2 bridge.

Standard library only. All decisions use Fraction equality. Float fields are
for display only. A prescribed finite graph connection is not a solution of
Kaluza-Klein gravity. Closed-path values do not encode arbitrary interventions.
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import argparse
import json
import sys

HERE = Path(__file__).resolve().parent
ONE = (F(1), F(0), F(0), F(0))
ZERO = (F(0),) * 4
BASIS = [tuple(F(int(i == j + 1)) for i in range(4)) for j in range(3)]


def q(values):
    return tuple(F(x) for x in values)


def eps(i, j, k):
    if len({i, j, k}) < 3:
        return 0
    return 1 if (i, j, k) in ((0, 1, 2), (1, 2, 0), (2, 0, 1)) else -1


def mul(a, b):
    return (a[0] * b[0] - sum(a[i] * b[i] for i in range(1, 4)),) + tuple(
        a[0] * b[i + 1] + b[0] * a[i + 1] +
        sum(F(eps(i, j, k)) * a[j + 1] * b[k + 1]
            for j in range(3) for k in range(3)) for i in range(3))


def conjugate(a):
    return (a[0], -a[1], -a[2], -a[3])


def norm2(a):
    return sum(x * x for x in a)


def rotate(g, v):
    value = mul(mul(g, (F(0),) + tuple(v)), conjugate(g))
    assert value[0] == 0
    return value[1:]


def qconj(g, a):
    return mul(mul(g, a), conjugate(g))


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


def rotation(g):
    return transpose([list(rotate(g, basis[1:])) for basis in BASIS])


def tensor(u, v):
    return [[u[i] * v[j] for j in range(3)] for i in range(3)]


def add(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(k, a):
    return [[k * x for x in row] for row in a]


def residual(t):
    trace = sum(t[i][i] for i in range(3))
    return [[(t[i][j] + t[j][i]) / 2 - (trace / 3 if i == j else 0)
             for j in range(3)] for i in range(3)]


def compression(t):
    result = [F(0)] * 4
    for i in range(3):
        for j in range(3):
            product = mul(BASIS[j], BASIS[i])
            result = [a + t[i][j] * b for a, b in zip(result, product)]
    return tuple(result)


def value_lift(value):
    return [[-value[0] / 3 * int(i == j) -
             sum(F(eps(i, j, k), 2) * value[k + 1] for k in range(3))
             for j in range(3)] for i in range(3)]


def insertion(t, probe):
    result = [F(0)] * 4
    for i in range(3):
        for j in range(3):
            product = mul(mul(BASIS[j], probe), BASIS[i])
            result = [a + t[i][j] * b for a, b in zip(result, product)]
    return tuple(result)


def response(s):
    columns = [insertion(s, basis) for basis in BASIS]
    assert all(column[0] == 0 for column in columns)
    return transpose([list(column[1:]) for column in columns])


def transport(g, t):
    r = rotation(g)
    return matmul(matmul(r, t), transpose(r))


def readout(unit, source, analyzer):
    assert norm2(unit) == 1
    return sum(x * y for x, y in zip(analyzer, rotate(unit, source)))


def complex_add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def complex_mul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def matrix2_mul(a, b):
    # Independent Gaussian-rational 2x2 representation, not qmul or rotation().
    return [[complex_add(complex_mul(a[i][0], b[0][j]),
                         complex_mul(a[i][1], b[1][j])) for j in range(2)] for i in range(2)]


def matrix2(unit):
    a, b, c, d = unit
    return [[(a, b), (c, d)], [(-c, d), (a, -b)]]


def matrix2_path(links, path):
    answer = matrix2(ONE)
    for start, end in zip(path[:-1], path[1:]):
        answer = matrix2_mul(matrix2(links[start, end]), answer)
    return answer


def response_readout(s, probe, analyzer):
    out = matmul(response(s), [[x] for x in probe])
    return sum(analyzer[i] * out[i][0] for i in range(3))


def graph(protocol):
    vertices = {"b": [0, 0], "x1": [1, 0], "x2": [1, 1],
                "y1": [-1, 0], "y2": [-1, 1], "z1": [0, -1],
                "z2": [1, -1], "r": [0, 2]}
    pairs = {
        "x": (q(["3/5", "4/5", 0, 0]), q(["5/13", 0, "12/13", 0])),
        "y": (q(["5/13", 0, 0, "12/13"]), q(["3/5", 0, "4/5", 0])),
        "z": (q(["3/5", 0, "4/5", 0]), q(["5/13", "12/13", 0, 0])),
    }
    links, loops = {}, {}
    for name, (first, second) in pairs.items():
        target = q(protocol["loop_targets"][name])
        closing = mul(target, conjugate(mul(second, first)))
        path = ["b", name + "1", name + "2", "b"]
        loops[name] = path
        for start, end, unit in zip(path[:-1], path[1:], [first, second, closing]):
            links[start, end] = unit
            links[end, start] = conjugate(unit)
    links["b", "r"] = q(["5/13", 0, "12/13", 0])
    links["r", "b"] = conjugate(links["b", "r"])
    return vertices, links, loops


def holonomy(links, path):
    result = ONE
    for start, end in zip(path[:-1], path[1:]):
        result = mul(links[start, end], result)
    return result


def stereographic(a, b, c):
    vector = (F(a), F(b), F(c))
    radius = sum(x * x for x in vector)
    return ((1 - radius) / (1 + radius),) + tuple(2 * x / (1 + radius) for x in vector)


def gauge_links(links, frames):
    return {(start, end): mul(mul(frames[end], unit), conjugate(frames[start]))
            for (start, end), unit in links.items()}


def packed(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, (list, tuple)):
        return [packed(x) for x in value]
    if isinstance(value, dict):
        return {str(k): packed(v) for k, v in value.items()}
    return value


def run(out):
    protocol_bytes = (HERE / "PROTOCOL.json").read_bytes()
    protocol = json.loads(protocol_bytes)
    out.mkdir(parents=True, exist_ok=False)
    vertices, links, loops = graph(protocol)
    loop = {name: holonomy(links, path) for name, path in loops.items()}
    checks = {}
    checks["all_links_are_exact_units"] = all(norm2(x) == 1 for x in links.values())
    checks["reverse_links_are_inverses"] = all(mul(links[b, a], u) == ONE for (a, b), u in links.items())
    checks["prescribed_loop_holonomies"] = all(loop[n] == q(protocol["loop_targets"][n]) for n in loop)
    probe, source, analyzer = q(protocol["probe"]), q(protocol["charge_source"]), q(protocol["analyzer"])
    values, tensors, residues, midpoint, records = {}, {}, {}, {}, {}
    for name in ("x", "y"):
        unit = loop[name]
        assert unit[0] == 0
        t = tensor(unit[1:], unit[1:])
        value, s = compression(t), residual(t)
        direct = mul(mul(unit, probe), unit)
        restored = insertion(add(value_lift(value), s), probe)
        values[name], tensors[name], residues[name], midpoint[name] = value, t, s, direct
        records[name] = {"loop": unit, "T": t, "S": s, "value": value,
                         "midpoint_output": direct,
                         "readout_without_probe": readout(value, source, analyzer),
                         "midpoint_readout": readout(direct, source, analyzer),
                         "appended_readout": readout(mul(probe, value), source, analyzer)}
        checks[name + "_direct_loop_and_compression_match"] = value == mul(unit, unit)
        checks[name + "_residual_in_kernel"] = compression(s) == ZERO
        checks[name + "_residual_response"] = response(s) == scale(F(-2), s)
        checks[name + "_coordinates_restore_tensor"] = add(value_lift(value), s) == t
        checks[name + "_coordinates_restore_midpoint_action"] = restored == direct
    checks["full_endpoint_holonomies_equal"] = values["x"] == values["y"] == q([-1, 0, 0, 0])
    checks["no_probe_readouts_equal"] = records["x"]["readout_without_probe"] == records["y"]["readout_without_probe"]
    checks["midpoint_readout_contrast"] = (records["x"]["midpoint_readout"], records["y"]["midpoint_readout"]) == (F(24, 25), F(-24, 25))
    checks["midpoint_trace_still_equal"] = midpoint["x"][0] == midpoint["y"][0]
    # An arbitrary identical suffix/prefix only sees the already completed value.
    appended = [stereographic(F(k, 5), F(k + 1, 7), F(2 - k, 9)) for k in range(5)]
    checks["all_appended_controls_equal"] = all(mul(c, values["x"]) == mul(c, values["y"]) and mul(values["x"], c) == mul(values["y"], c) for c in appended)
    value_only_insertion = insertion(value_lift(values["x"]), probe)
    checks["value_only_lift_is_not_a_unitary_prediction"] = norm2(value_only_insertion) == F(97, 225)
    connector_path = ["b", "r"]
    alternate_path = loops["z"] + ["r"]
    p, alternative = holonomy(links, connector_path), holonomy(links, alternate_path)
    sp, sq = transport(p, residues["x"]), transport(alternative, residues["x"])
    cp = rotate(p, (F(1), F(0), F(0)))
    a = response_readout(sp, cp, cp)
    b = response_readout(sq, cp, cp)
    checks["same_endpoints_different_transported_residuals"] = sp != sq
    checks["route_response_contrast"] = (a, b) == (F(-4, 3), F(956, 1875))
    checks["both_transports_leave_compressed_word_value_equal"] = compression(transport(p, tensors["x"])) == compression(transport(alternative, tensors["x"])) == values["x"]
    checks["transport_and_reverse_restore_residual"] = transport(conjugate(p), sp) == residues["x"]
    returned = transport(conjugate(p), sq)
    checks["loop_then_return_can_rotate_residual"] = returned == transport(loop["z"], residues["x"]) and returned != residues["x"]
    axis_p = rotate(p, BASIS[0][1:])
    axis_q = rotate(alternative, BASIS[0][1:])
    identity_third = [[F(int(i == j), 3) for j in range(3)] for i in range(3)]
    checks["ordinary_axis_tensor_calculation_matches"] = (add(tensor(axis_p, axis_p), scale(F(-1), identity_third)) == sp and
                                                         add(tensor(axis_q, axis_q), scale(F(-1), identity_third)) == sq)
    checks["residual_response_transport_covariant"] = response(sp) == transport(p, response(residues["x"]))
    matrix_checks = []
    for name in ("x", "y"):
        independent_loop = matrix2_path(links, loops[name])
        matrix_checks += [independent_loop == matrix2(loop[name]),
                          matrix2_mul(independent_loop, independent_loop) == matrix2(values[name]),
                          matrix2_mul(matrix2_mul(independent_loop, matrix2(probe)), independent_loop) == matrix2(midpoint[name])]
    checks["independent_exact_complex_matrix_representation"] = all(matrix_checks)
    # Abelian control: all factors lie in one complex/U(1) subalgebra.
    ua = q(["3/5", "4/5", 0, 0])
    ub = tuple(-x for x in conjugate(ua))
    ui = BASIS[0]
    checks["U1_control_no_midpoint_contrast"] = mul(mul(ub, probe), ua) == mul(mul(ui, probe), ui) == mul(probe, q([-1, 0, 0, 0]))
    gauge_records = []
    for trial in range(protocol["gauge_trials"]):
        frames = {name: stereographic(F(index + 1, trial + 3), F(trial - index, 7), F(index + trial + 2, 11))
                  for index, name in enumerate(vertices)}
        transformed = gauge_links(links, frames)
        gb, gr = frames["b"], frames["r"]
        local_probe = qconj(gb, probe)
        local_source, local_analyzer = rotate(gb, source), rotate(gb, analyzer)
        predicates = []
        for name in ("x", "y"):
            h = holonomy(transformed, loops[name])
            tt = tensor(h[1:], h[1:])
            ss = residual(tt)
            inserted = mul(mul(h, local_probe), h)
            predicates += [h == qconj(gb, loop[name]), tt == transport(gb, tensors[name]),
                           ss == transport(gb, residues[name]), compression(tt) == qconj(gb, values[name]),
                           insertion(add(value_lift(compression(tt)), ss), local_probe) == inserted,
                           readout(inserted, local_source, local_analyzer) == records[name]["midpoint_readout"],
                           response(ss) == scale(F(-2), ss)]
        pp = holonomy(transformed, connector_path)
        qq = holonomy(transformed, alternate_path)
        state = transport(gb, residues["x"])
        probe_r = rotate(gr, cp)
        predicates += [transport(pp, state) == transport(gr, sp),
                       transport(qq, state) == transport(gr, sq),
                       response_readout(transport(pp, state), probe_r, probe_r) == a,
                       response_readout(transport(qq, state), probe_r, probe_r) == b]
        passed = all(predicates)
        checks["independent_local_gauge_trial_" + str(trial)] = passed
        gauge_records.append({"trial": trial, "vertices": len(vertices), "exact_equalities": len(predicates), "all_pass": passed})
    result = {
        "id": protocol["id"], "status": "PASS" if all(checks.values()) else "FAIL",
        "source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "protocol_sha256": sha256(protocol_bytes).hexdigest(),
        "runtime": {"python": sys.version, "arithmetic": "fractions.Fraction; exact; floats never used for assertions"},
        "checks": checks, "gauge_trials": gauge_records,
        "display_summary": {"unprobed": [float(records[n]["readout_without_probe"]) for n in ("x", "y")],
                            "midpoint": [float(records[n]["midpoint_readout"]) for n in ("x", "y")],
                            "appended": [float(records[n]["appended_readout"]) for n in ("x", "y")],
                            "same_endpoint_routes_residual_response": [float(a), float(b)]},
        "independent_audit": False, "Core_modified": False,
        "interpretation": "A gauge-covariant exterior encoding of prescribed loop protocols. Equal completed holonomy has equal appended evolution; the difference concerns midpoint interventions and connection transport of the retained protocol descriptor.",
        "scope_limits": protocol["scope_limits"]
    }
    certificate = {"paths": records, "probe": probe, "source": source, "analyzer": analyzer,
                   "canonical_value_only_insert": value_only_insertion,
                   "canonical_value_only_insert_norm2": norm2(value_only_insertion),
                   "transport": {"P": p, "Q": alternative, "S_at_b": residues["x"],
                                 "S_via_P": sp, "S_via_Q": sq, "common_probe_and_analyzer": cp,
                                 "response_via_P": a, "response_via_Q": b}}
    graph_data = {"vertices": vertices,
                  "directed_links": [{"from": s, "to": t, "U": unit} for (s, t), unit in links.items()],
                  "loops": loops, "connector_path": connector_path, "alternate_path": alternate_path}
    for name, data in (("RESULTS.json", result), ("EXACT_CERTIFICATE.json", packed(certificate)),
                       ("CONNECTION.json", packed(graph_data))):
        (out / name).write_bytes((json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
    print(json.dumps({"status": result["status"], "checks": len(checks),
                      "failed": [k for k, v in checks.items() if not v],
                      "display_summary": result["display_summary"],
                      "gauge_trials": gauge_records}, indent=2))
    if not all(checks.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    run(parser.parse_args().out)
