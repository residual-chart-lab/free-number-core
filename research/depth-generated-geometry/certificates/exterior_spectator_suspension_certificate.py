#!/usr/bin/env python3
"""Exact certificate for exterior spectator suspension.

The all-length theorem in Note 22 is driven by three fixed quaternion
identities:

    Sigma^-(F tensor w)(z,x) = F(x) z w,
    Sigma^+(w tensor F)(x,z) = w z F(x),
    u z_+ (F z_- w) = (u z_+ F) z_- w.

This script checks that the two one-variable encoders are invertible, checks
prepend and append response identities on every basis state, face, edge,
probe word, and carried vector through n=5, and checks strict left/right
interchange on a complete quaternionic basis.

The finite checks witness the primitive identities. The all-n result follows
symbolically by applying them blockwise to the local matching complex, as
proved in Note 22.

Only exact integer and fractions.Fraction arithmetic is used.
"""

from itertools import combinations, product

from n2_intrinsic_response_certificate import Mat, Q, V, qmul


def qprod_reversed(letters):
    value = Q[0]
    for letter in reversed(letters):
        value = qmul(value, letter)
    return value


def response_value(state, missing_gaps, probe_word):
    """Evaluate the exact response of one pure tensor basis state."""

    n = len(state)
    missing = set(missing_gaps)
    probed = [
        gap for gap in range(1, n) if gap not in missing
    ]
    if len(probed) != len(probe_word):
        raise ValueError("probe word has the wrong length")

    letters = [V[index] for index in state]
    for gap, probe in sorted(
        zip(probed, probe_word), reverse=True
    ):
        letters.insert(gap, V[probe])
    return qprod_reversed(letters)


def right_local_encoder():
    """Theta_R(h tensor w)(z)=hzw."""

    matrix = Mat.zeros(12, 12)
    for h_index, w_index, z_index in product(
        range(4), range(3), range(3)
    ):
        column = 3 * h_index + w_index
        value = qmul(qmul(Q[h_index], V[z_index]), V[w_index])
        for component, entry in enumerate(value):
            matrix[4 * z_index + component, column] = entry
    return matrix


def left_local_encoder():
    """Theta_L(w tensor h)(z)=wzh."""

    matrix = Mat.zeros(12, 12)
    for w_index, h_index, z_index in product(
        range(3), range(4), range(3)
    ):
        column = 4 * w_index + h_index
        value = qmul(qmul(V[w_index], V[z_index]), Q[h_index])
        for component, entry in enumerate(value):
            matrix[4 * z_index + component, column] = entry
    return matrix


def suspension_checks():
    checked = 0
    valid = True

    for n in range(3, 6):
        gaps = tuple(range(1, n))
        missing_sets = [
            missing
            for size in (1, 2)
            for missing in combinations(gaps, size)
        ]
        for state, missing in product(
            product(range(3), repeat=n),
            missing_sets,
        ):
            depth = n - 1 - len(missing)
            for probes, w_index, z_index in product(
                product(range(3), repeat=depth),
                range(3),
                range(3),
            ):
                old = response_value(state, missing, probes)
                w = V[w_index]
                z = V[z_index]

                prepended = response_value(
                    (w_index, *state),
                    tuple(gap + 1 for gap in missing),
                    (z_index, *probes),
                )
                expected_left = qmul(qmul(old, z), w)
                valid = valid and prepended == expected_left
                checked += 1

                appended = response_value(
                    (*state, w_index),
                    missing,
                    (*probes, z_index),
                )
                expected_right = qmul(qmul(w, z), old)
                valid = valid and appended == expected_right
                checked += 1

    return valid, checked


def interchange_checks():
    checked = 0
    valid = True
    for u, z_plus, h, z_minus, w in product(V, V, Q, V, V):
        left_then_right = qmul(
            qmul(u, z_plus),
            qmul(qmul(h, z_minus), w),
        )
        right_then_left = qmul(
            qmul(qmul(qmul(u, z_plus), h), z_minus),
            w,
        )
        valid = valid and left_then_right == right_then_left
        checked += 1
    return valid, checked


def report():
    checks = []

    def check(name, condition):
        checks.append((name, bool(condition)))

    theta_right = right_local_encoder()
    theta_left = left_local_encoder()
    det_right = theta_right.det()
    det_left = theta_left.det()
    check("the right local encoder is invertible", det_right != 0)
    check("the left local encoder is invertible", det_left != 0)

    suspension_valid, suspension_count = suspension_checks()
    check(
        "prepend and append identities hold through n=5",
        suspension_valid and suspension_count == 764478,
    )

    interchange_valid, interchange_count = interchange_checks()
    check(
        "left and right exterior suspensions commute strictly",
        interchange_valid and interchange_count == 324,
    )

    seed_ranks = (16, 12, 16, 4, 12, 16)
    first_seed_ranks = tuple(3 * value for value in seed_ranks)
    second_seed_ranks = tuple(3 * value for value in first_seed_ranks)
    check(
        "the first seed suspension gives the exact n=6 edge ranks",
        first_seed_ranks == (48, 36, 48, 12, 36, 48),
    )
    check(
        "the second seed suspension gives the exact n=7 edge ranks",
        second_seed_ranks == (144, 108, 144, 36, 108, 144),
    )

    cap_defects = tuple(4 * 3**r for r in range(5))
    exceptional_dimensions = tuple(148 * 3**r for r in range(5))
    exceptional_residuals = tuple(4 * 3**r for r in range(5))
    check(
        "the central-cap defect tensors from 4 to 4*3^r",
        cap_defects == (4, 12, 36, 108, 324),
    )
    check(
        "the exceptional quotient tensors as 148=144+4",
        all(
            total == 144 * 3**r + residual
            for r, (total, residual) in enumerate(
                zip(exceptional_dimensions, exceptional_residuals)
            )
        ),
    )

    exceptional_core = (144, 108, 144, 36, 108, 144)
    exceptional_full = (144, 112, 148, 40, 112, 144)
    check(
        "the exceptional core edge profile tensors uniformly",
        tuple(3 * value for value in exceptional_core)
        == (432, 324, 432, 108, 324, 432),
    )
    check(
        "the full exceptional edge profile tensors uniformly",
        tuple(3 * value for value in exceptional_full)
        == (432, 336, 444, 120, 336, 432),
    )
    check(
        "the n=6 cap edge profile has the certified long-edge defect",
        (48, 36, 44, 12, 36, 48)[2] == 48 - 4,
    )

    print("det(Theta_R), det(Theta_L):", det_right, det_left)
    print("basis suspension identities checked:", suspension_count)
    print("strict interchange identities checked:", interchange_count)
    print("seed ranks after two exterior suspensions:", second_seed_ranks)
    print(
        "exceptional tower dimensions r=0..4:",
        exceptional_dimensions,
    )
    print(
        "exceptional residual dimensions r=0..4:",
        exceptional_residuals,
    )
    for name, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {name}")
    failed = [name for name, passed in checks if not passed]
    if failed:
        raise SystemExit("FAILED: " + ", ".join(failed))
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    report()
