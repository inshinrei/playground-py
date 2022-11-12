import math

from typing import List


Vector = List[float]
height_weight_age = [70, 170, 40]
grades = [95, 80, 75, 62]


def add(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w), 'vectors must be the same len'

    return [v_i + w_i for v_i, w_i in zip(v, w)]


def subtract(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w), 'vectors must be the same len'

    return [v_i - w_i for v_i, w_i in zip(v, w)]


def vectors_sum(vectors: List[Vector]) -> Vector:
    assert vectors, 'no vectors provided'

    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), 'vectors must be the same sizes'

    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]


assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]
assert vectors_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]


def scalar_multiply(c: float, v: Vector) -> Vector:
    return [c * v_i for v_i in v]


def vectors_mean(vectors: List[Vector]) -> Vector:
    n = len(vectors)
    return scalar_multiply(1/n, vectors_sum(vectors))


def dot(v: Vector, w: Vector) -> float:
    assert len(v) == len(w), 'vectors must be the same len'

    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v: Vector) -> float:
    return dot(v, v)


def magnitude(v: Vector) -> float:
    return math.sqrt(sum_of_squares(v))


assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]
assert vectors_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]
assert dot([1, 2, 3], [4, 5, 6]) == 32
assert sum_of_squares([1, 2, 3]) == 14
assert magnitude([3, 4]) == 5
