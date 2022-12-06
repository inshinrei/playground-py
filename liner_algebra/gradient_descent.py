from typing import Callable, List

from liner_algebra.vector import Vector, dot


def sum_of_squares(v: Vector) -> float:
    return dot(v, v)


def difference_quotient(f: Callable[[float], float], x: float, h: float) -> float:
    return (f(x + h) - f(x)) / h


def partial_difference_quotient(f: Callable[[List[float]], float], V: List[float], i: float, h: float) -> float:
    w = [v_j + (h if j == i else 0) for j, v_j in enumerate(V)]
    return (f(w) - f(V)) / h


def square(x: float) -> float:
    return x * x


def derivative(x: float) -> float:
    return 2 * x
