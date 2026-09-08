#!/usr/bin/env python3
"""Exact certificate for the intrinsic depth tower at n=2.

Conventions agree with Free Numbers Core v1:

    m_2(e_p | e_a) = e_a e_p,
    A_2(e_p | e_a)(d) = e_a d e_p.

The certificate checks, over exact rational arithmetic, that:

1. im(A_2) consists exactly of maps F: V -> H whose imaginary part
   M_F: V -> V is self-adjoint;
2. the intrinsic truncation tau(F) = sum_a e_a F(e_a) intertwines A_2
   with m_2;
3. tau is onto H and has a five-dimensional kernel;
4. the kernel is the symmetric trace-free layer, and A_2 acts there
   by the coefficient -2;
5. the basis-free reconstruction tensor

       T_F = 1/2 ((tr M_F) I - M_F + [alpha_F]_x)

   recovers the unique length-two representative.
"""

from fractions import Fraction


class Mat:
    """Small exact matrix class over fractions.Fraction."""

    def __init__(self, rows):
        self.data = [[Fraction(value) for value in row] for row in rows]
        self.nrows = len(self.data)
        self.ncols = len(self.data[0]) if self.nrows else 0
        if any(len(row) != self.ncols for row in self.data):
            raise ValueError("ragged matrix")

    @classmethod
    def zeros(cls, nrows, ncols):
        return cls([[0 for _ in range(ncols)] for _ in range(nrows)])

    @classmethod
    def eye(cls, size):
        out = cls.zeros(size, size)
        for idx in range(size):
            out[idx, idx] = 1
        return out

    @classmethod
    def diag(cls, *values):
        out = cls.zeros(len(values), len(values))
        for idx, value in enumerate(values):
            out[idx, idx] = value
        return out

    def __getitem__(self, key):
        row, col = key
        return self.data[row][col]

    def __setitem__(self, key, value):
        row, col = key
        self.data[row][col] = Fraction(value)

    def __mul__(self, other):
        if self.ncols != other.nrows:
            raise ValueError("incompatible matrix dimensions")
        out = Mat.zeros(self.nrows, other.ncols)
        for row in range(self.nrows):
            for mid in range(self.ncols):
                value = self[row, mid]
                if value == 0:
                    continue
                for col in range(other.ncols):
                    out[row, col] += value * other[mid, col]
        return out

    def __eq__(self, other):
        return (
            isinstance(other, Mat)
            and self.nrows == other.nrows
            and self.ncols == other.ncols
            and self.data == other.data
        )

    def row_join(self, other):
        if self.nrows != other.nrows:
            raise ValueError("row counts differ")
        return Mat([left + right for left, right in zip(self.data, other.data)])

    def rank(self):
        work = [row[:] for row in self.data]
        pivot_row = 0
        for col in range(self.ncols):
            pivot = next(
                (row for row in range(pivot_row, self.nrows) if work[row][col] != 0),
                None,
            )
            if pivot is None:
                continue
            work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
            pivot_value = work[pivot_row][col]
            work[pivot_row] = [value / pivot_value for value in work[pivot_row]]
            for row in range(self.nrows):
                if row == pivot_row or work[row][col] == 0:
                    continue
                factor = work[row][col]
                work[row] = [
                    value - factor * pivot_entry
                    for value, pivot_entry in zip(work[row], work[pivot_row])
                ]
            pivot_row += 1
            if pivot_row == self.nrows:
                break
        return pivot_row

    def det(self):
        if self.nrows != self.ncols:
            raise ValueError("determinant requires a square matrix")
        work = [row[:] for row in self.data]
        result = Fraction(1)
        sign = 1
        for col in range(self.ncols):
            pivot = next(
                (row for row in range(col, self.nrows) if work[row][col] != 0),
                None,
            )
            if pivot is None:
                return Fraction(0)
            if pivot != col:
                work[col], work[pivot] = work[pivot], work[col]
                sign *= -1
            pivot_value = work[col][col]
            result *= pivot_value
            for row in range(col + 1, self.nrows):
                if work[row][col] == 0:
                    continue
                factor = work[row][col] / pivot_value
                for inner_col in range(col, self.ncols):
                    work[row][inner_col] -= factor * work[col][inner_col]
        return sign * result


def levi_civita(a, b, c):
    if len({a, b, c}) < 3:
        return 0
    inversions = int(a > b) + int(a > c) + int(b > c)
    return -1 if inversions % 2 else 1


Q = [
    (1, 0, 0, 0),
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1),
]
V = Q[1:]


def qmul(x, y):
    a0, a1, a2, a3 = x
    b0, b1, b2, b3 = y
    return (
        a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3,
        a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2,
        a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1,
        a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0,
    )


def response_index(d_idx, q_comp):
    return 4 * d_idx + q_comp


def tensor_index(first_idx, last_idx):
    return 3 * first_idx + last_idx


def build_A2():
    matrix = Mat.zeros(12, 9)
    for first_idx, first in enumerate(V):
        for last_idx, last in enumerate(V):
            col = tensor_index(first_idx, last_idx)
            for d_idx, d in enumerate(V):
                out = qmul(qmul(last, d), first)
                for comp in range(4):
                    matrix[response_index(d_idx, comp), col] = out[comp]
    return matrix


def build_m2():
    matrix = Mat.zeros(4, 9)
    for first_idx, first in enumerate(V):
        for last_idx, last in enumerate(V):
            col = tensor_index(first_idx, last_idx)
            out = qmul(last, first)
            for comp in range(4):
                matrix[comp, col] = out[comp]
    return matrix


def build_self_adjoint_constraints():
    """C F = 0 iff Im(F): V -> V is self-adjoint."""
    matrix = Mat.zeros(3, 12)
    for row, (left, right) in enumerate(((0, 1), (0, 2), (1, 2))):
        # M_{left,right} - M_{right,left}
        matrix[row, response_index(right, left + 1)] = 1
        matrix[row, response_index(left, right + 1)] = -1
    return matrix


def build_intrinsic_parameterization():
    """Coordinates: alpha_0..2, M_00,M_11,M_22,M_01,M_02,M_12."""
    matrix = Mat.zeros(12, 9)

    for d_idx in range(3):
        matrix[response_index(d_idx, 0), d_idx] = 1

    symmetric_slots = {
        (0, 0): 3,
        (1, 1): 4,
        (2, 2): 5,
        (0, 1): 6,
        (1, 0): 6,
        (0, 2): 7,
        (2, 0): 7,
        (1, 2): 8,
        (2, 1): 8,
    }
    for (out_idx, in_idx), col in symmetric_slots.items():
        matrix[response_index(in_idx, out_idx + 1), col] = 1

    return matrix


def build_tau():
    """tau(F) = sum_a e_a F(e_a)."""
    matrix = Mat.zeros(4, 12)
    for d_idx, e_d in enumerate(V):
        for in_comp, basis_q in enumerate(Q):
            out = qmul(e_d, basis_q)
            for out_comp in range(4):
                matrix[out_comp, response_index(d_idx, in_comp)] += out[out_comp]
    return matrix


def build_reconstruction():
    """Map (alpha,M_sym) to coefficients T_{p a} of sum T(e_a)|e_a."""
    matrix = Mat.zeros(9, 9)

    # Symmetric part: 1/2 ((tr M) I - M).
    for first_idx in range(3):
        for last_idx in range(3):
            row = tensor_index(first_idx, last_idx)
            if first_idx == last_idx:
                for diag_col in (3, 4, 5):
                    matrix[row, diag_col] += Fraction(1, 2)

            m_col = {
                (0, 0): 3,
                (1, 1): 4,
                (2, 2): 5,
                (0, 1): 6,
                (1, 0): 6,
                (0, 2): 7,
                (2, 0): 7,
                (1, 2): 8,
                (2, 1): 8,
            }[(first_idx, last_idx)]
            matrix[row, m_col] -= Fraction(1, 2)

            # Skew part: 1/2 [alpha]_x, where [alpha]_x(v)=alpha x v.
            for alpha_idx in range(3):
                matrix[row, alpha_idx] += (
                    Fraction(1, 2)
                    * levi_civita(first_idx, alpha_idx, last_idx)
                )

    return matrix


def build_section():
    """q=a+w maps to F(d)=<w,d>-(a/3)d."""
    matrix = Mat.zeros(12, 4)
    for d_idx in range(3):
        matrix[response_index(d_idx, 0), d_idx + 1] = 1
        matrix[response_index(d_idx, d_idx + 1), 0] = -Fraction(1, 3)
    return matrix


def build_stf_tensors_and_responses():
    stf_matrices = [
        Mat.diag(1, -1, 0),
        Mat.diag(1, 0, -1),
        Mat([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
        Mat([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
        Mat([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
    ]

    tensors = Mat.zeros(9, 5)
    expected_responses = Mat.zeros(12, 5)
    for col, S in enumerate(stf_matrices):
        for first_idx in range(3):
            for last_idx in range(3):
                tensors[tensor_index(first_idx, last_idx), col] = S[first_idx, last_idx]
        for in_idx in range(3):
            for out_idx in range(3):
                expected_responses[response_index(in_idx, out_idx + 1), col] = -2 * S[out_idx, in_idx]
    return tensors, expected_responses


def main():
    checks = []

    def check(name, condition):
        checks.append((name, bool(condition)))

    A2 = build_A2()
    m2 = build_m2()
    C = build_self_adjoint_constraints()
    P = build_intrinsic_parameterization()
    tau = build_tau()
    reconstruct = build_reconstruction()
    section = build_section()
    stf_tensors, stf_expected = build_stf_tensors_and_responses()

    check("A2 has rank 9", A2.rank() == 9)
    check("self-adjoint constraints have rank 3", C.rank() == 3)
    check("A2 responses satisfy the intrinsic constraints", C * A2 == Mat.zeros(3, 9))
    check("intrinsic parameterization has rank 9", P.rank() == 9)
    check("intrinsic space equals im(A2)", A2.row_join(P).rank() == 9)

    check("tau intertwines A2 with m2", tau * A2 == m2)
    check("tau is onto on the intrinsic space", (tau * P).rank() == 4)
    check("birth layer has dimension 5", 9 - (tau * P).rank() == 5)
    check("intrinsic section is admissible", C * section == Mat.zeros(3, 4))
    check("intrinsic section splits tau", tau * section == Mat.eye(4))

    check("reconstruction recovers every intrinsic response", A2 * reconstruct == P)
    check("reconstruction is an isomorphism", reconstruct.det() != 0)

    check("STF tensors lie in the compression kernel", m2 * stf_tensors == Mat.zeros(4, 5))
    check("A2 acts by -2 on the STF layer", A2 * stf_tensors == stf_expected)
    check("STF responses span the birth layer", stf_expected.rank() == 5)
    check("STF responses are killed by tau", tau * stf_expected == Mat.zeros(4, 5))

    all_ok = True
    for name, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {name}")
        all_ok = all_ok and passed

    print("ALL CHECKS PASSED" if all_ok else "SOME CHECK FAILED")


if __name__ == "__main__":
    main()
