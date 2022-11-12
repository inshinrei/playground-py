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


def vector_sum(vectors: List[Vector]) -> Vector:
    assert vectors, 'no vectors provided'

    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), 'vectors must be the same sizes'

    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]


assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]
assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]
