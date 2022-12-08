import random
from typing import Callable, TypeVar, Iterator, List

from liner_algebra.vector import Vector, dot, add, scalar_multiply


def sum_of_squares(v: Vector) -> float:
    return dot(v, v)


def difference_quotient(f: Callable[[float], float], x: float, h: float) -> float:
    return (f(x + h) - f(x)) / h


def partial_difference_quotient(f: Callable[[Vector], float], V: Vector, i: float, h: float) -> float:
    w = [v_j + (h if j == i else 0) for j, v_j in enumerate(V)]
    return (f(w) - f(V)) / h


def square(x: float) -> float:
    return x * x


def derivative(x: float) -> float:
    return 2 * x


def estimate_gradient(f: Callable[[Vector], float], V: Vector, h: float = 0.0001):
    return [partial_difference_quotient(f, V, i, h) for i in range(len(V))]


def gradient_step(V: Vector, gradient: Vector, step_size: float) -> Vector:
    assert len(V) == len(gradient)
    step = scalar_multiply(step_size, gradient)
    return add(V, step)


def sum_of_squares_gradient(V: Vector) -> Vector:
    return [2 * v_i for v_i in V]


def linear_gradient(x: float, y: float, theta: Vector) -> Vector:
    slope, intercept = theta
    predicted = slope * x + intercept
    error = (predicted - y)
    return [2 * error * x, 2 * error]


T = TypeVar('T')


def mini_batches(dataset: List[T], batch_size: int, shuffle: bool = True) -> Iterator[List[T]]:
    batch_starts = [start for start in range(0, len(dataset), batch_size)]

    if shuffle:
        random.shuffle(batch_starts)

    for start in batch_starts:
        end = start + batch_size
        yield dataset[start:end]
