from __future__ import annotations

import sympy as s


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def require_matrix_equal(actual: s.Matrix, expected: s.Matrix, message: str) -> None:
    require(actual == expected, f"{message}\nactual=\n{actual}\nexpected=\n{expected}")


def check_chapter_1() -> None:
    A = s.Matrix([[1, 1, 1], [2, -1, 1], [1, 2, -1]])
    b = s.Matrix([3, 0, 5])
    sol, params = A.gauss_jordan_solve(b)
    require(params.shape == (0, 1), "第 1 章例 1 应为唯一解")
    require_matrix_equal(sol, s.Matrix([1, 2, 0]), "第 1 章例 1 解答错误")

    A = s.Matrix([[1, 1, 1], [2, 2, 2], [1, -1, 1]])
    basis = A.nullspace()
    require(len(basis) == 1, "第 1 章例 2 的基础解系向量个数应为 1")
    require_matrix_equal(basis[0], s.Matrix([-1, 0, 1]), "第 1 章例 2 基础解系错误")

    A = s.Matrix([[1, 1, 1], [1, s.Symbol("a"), 2], [1, 2, s.Symbol("a")]])
    require(s.factor(A.det()) == s.Symbol("a") * (s.Symbol("a") - 2), "第 1 章参数例题行列式分解错误")

    a = s.symbols("a")
    A = s.Matrix([[1, 1, 1], [1, a, 2], [1, 2, a]])
    b = s.Matrix([1, 2, 2])
    A0 = A.subs(a, 0)
    A2 = A.subs(a, 2)
    require(A0.rank() < A0.row_join(b).rank(), "第 1 章参数例题中 a=0 应无解")
    require(A2.rank() == A2.row_join(b).rank() == 2, "第 1 章参数例题中 a=2 应有无穷多解")
    tau = s.symbols("tau")
    vec = s.Matrix([0, 1 - tau, tau])
    require_matrix_equal(A2 * vec, b, "第 1 章参数例题中 a=2 的通解提示错误")

    # Exercise A1
    A = s.Matrix([[1, 1, 1], [2, 3, 1], [1, 2, 0]])
    b = s.Matrix([1, 3, 2])
    tau = s.symbols("tau")
    vec = s.Matrix([0, 1, 0]) + tau * s.Matrix([-2, 1, 1])
    require_matrix_equal(A * vec, b, "第 1 章 A1 通解提示错误")
    require(A.rank() == A.row_join(b).rank() == 2, "第 1 章 A1 应为无穷多解")

    # Exercise B1
    A = s.Matrix([[1, 1, 1], [2, a + 1, 3], [1, 2, a]])
    b = s.Matrix([1, 3, 2])
    A0 = A.subs(a, 0)
    A2 = A.subs(a, 2)
    require(A0.rank() < A0.row_join(b).rank(), "第 1 章 B1 中 a=0 应无解")
    require(A2.rank() == A2.row_join(b).rank() == 2, "第 1 章 B1 中 a=2 应有无穷多解")
    tau = s.symbols("tau")
    vec = s.Matrix([0, 1 - tau, tau])
    require_matrix_equal(A2 * vec, b, "第 1 章 B1 中 a=2 的通解提示错误")


def check_chapter_2() -> None:
    A = s.Matrix([[1, 1, 0], [0, 1, 1], [1, 0, 1]])
    expected_inverse = s.Rational(1, 2) * s.Matrix([[1, -1, 1], [1, 1, -1], [-1, 1, 1]])
    require_matrix_equal(A.inv(), expected_inverse, "第 2 章例 4 逆矩阵错误")
    require(A.det() == 2, "第 2 章例 5 行列式错误")

    left = s.Matrix([[1, 1, 0], [0, 1, 1], [1, 0, 1]])
    right = s.Matrix([[2, 0, 1], [1, 1, 0], [0, 2, 1]])
    require_matrix_equal(left * right, s.Matrix([[3, 1, 1], [1, 3, 1], [2, 2, 2]]), "第 2 章 A1 乘法结果错误")

    A = s.Matrix([[1, 1, 0], [0, 1, 1], [0, 0, 1]])
    B = s.Matrix([[2, 1, 0], [1, 1, 1], [0, 2, 1]])
    require_matrix_equal(B * A.inv(), s.Matrix([[2, -1, 1], [1, 0, 1], [0, 2, -1]]), "第 2 章 B2 矩阵方程结果错误")


def check_chapter_3() -> None:
    A = s.Matrix([[1, 1, 0], [0, 2, 1], [0, 0, 3]])
    P = s.Matrix([[1, 1, 1], [0, 1, 2], [0, 0, 2]])
    D = s.diag(1, 2, 3)
    require_matrix_equal(P.inv() * A * P, D, "第 3 章例 7 对角化结果错误")

    A = s.Matrix([[2, 1, 0], [0, 2, 0], [0, 0, 1]])
    eigspace_dim = (A - 2 * s.eye(3)).nullspace()
    require(len(eigspace_dim) == 1, "第 3 章例 8 中 lambda=2 的特征空间维数应为 1")

    a = s.symbols("a")
    A = s.Matrix([[1, a, 0], [0, 1, 1], [0, 0, 2]])
    require((A.subs(a, 0) - s.eye(3)).nullspace().__len__() == 2, "第 3 章参数题中 a=0 应可对角化")
    require((A.subs(a, 1) - s.eye(3)).nullspace().__len__() == 1, "第 3 章参数题中 a!=0 时 lambda=1 的几何重数应为 1")


def check_chapter_4() -> None:
    A = s.Matrix([[2, 1, 0], [1, 2, 0], [0, 0, 3]])
    Q = s.Matrix(
        [
            [s.sqrt(2) / 2, s.sqrt(2) / 2, 0],
            [-s.sqrt(2) / 2, s.sqrt(2) / 2, 0],
            [0, 0, 1],
        ]
    )
    require_matrix_equal(Q.T * A * Q, s.diag(1, 3, 3), "第 4 章例 9 正交对角化结果错误")

    A = s.Matrix([[2, 0, 0], [0, 1, 1], [0, 1, 1]])
    Q = s.Matrix(
        [
            [1, 0, 0],
            [0, s.sqrt(2) / 2, s.sqrt(2) / 2],
            [0, s.sqrt(2) / 2, -s.sqrt(2) / 2],
        ]
    )
    require_matrix_equal(Q.T * A * Q, s.diag(2, 2, 0), "第 4 章补充例题正交对角化结果错误")

    v1 = s.Matrix([1, 1, 0])
    v2 = s.Matrix([1, 0, 0])
    u1 = v1
    u2 = v2 - (v2.dot(u1) / u1.dot(u1)) * u1
    require(u1.dot(u2) == 0, "第 4 章 Gram-Schmidt 例题中正交化结果错误")
    e1 = u1 / s.sqrt(u1.dot(u1))
    e2 = (2 * u2) / s.sqrt((2 * u2).dot(2 * u2))
    require(e1.dot(e2) == 0, "第 4 章 Gram-Schmidt 例题中单位正交化结果错误")
    require(e1.dot(e1) == 1 and e2.dot(e2) == 1, "第 4 章 Gram-Schmidt 例题中单位化结果错误")


def check_chapter_5() -> None:
    A = s.Matrix([[2, 1, 0], [1, 2, -1], [0, -1, 2]])
    require(A.det() == 4, "第 5 章例 10 行列式错误")
    require(A[:1, :1].det() > 0 and A[:2, :2].det() > 0 and A.det() > 0, "第 5 章例 10 顺序主子式判断错误")

    a = s.symbols("a", real=True)
    A = s.Matrix([[2, a, 0], [a, 3, 1], [0, 1, 2]])
    require(s.simplify(A.det() - (10 - 2 * a**2)) == 0, "第 5 章参数正定题行列式错误")

    A = s.Matrix([[1, a, 0], [a, 2, 1], [0, 1, 3]])
    require(s.simplify(A.det() - (5 - 3 * a**2)) == 0, "第 5 章 B2 顺序主子式计算错误")


def main() -> None:
    check_chapter_1()
    check_chapter_2()
    check_chapter_3()
    check_chapter_4()
    check_chapter_5()
    print("All checked linear algebra examples and answer hints passed.")


if __name__ == "__main__":
    main()
