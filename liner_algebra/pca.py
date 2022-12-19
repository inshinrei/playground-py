from typing import Tuple, List

import tqdm

from liner_algebra.gradient_descent import gradient_step
from liner_algebra.statistics import standard_deviation
from liner_algebra.vector import vectors_mean, Vector, subtract, magnitude, dot, scalar_multiply


def scale(data: List[Vector]) -> Tuple[Vector, Vector]:
    dim = len(data[0])

    means = vectors_mean(data)
    stdevs = [standard_deviation([vector[i] for vector in data]) for i in range(dim)]

    return means, stdevs


vectors = [[-3, -1, 1], [-1, 0, 1], [1, 1, 1]]
means_0, stdevs_0 = scale(vectors)

assert means_0 == [-1, 0, 1]
assert stdevs_0 == [2, 1, 0]


def rescale(data: List[Vector]) -> List[Vector]:
    dim = len(data[0])
    means, stdevs = scale(data)

    rescaled = [vector[:] for vector in data]

    for vector in rescaled:
        for i in range(dim):
            if stdevs[i] > 0:
                vector[i] = (vector[i] - means[i]) / stdevs[i]

    return rescaled


means_1, stdevs_1 = scale(rescale(vectors))
assert means_1 == [0, 0, 1]
assert stdevs_1 == [1, 1, 0]


def de_mean(data: List[Vector]) -> List[Vector]:
    mean = vectors_mean(data)
    return [subtract(vector, mean) for vector in data]


def direction(w: Vector) -> Vector:
    mag = magnitude(w)
    return [w_i / mag for w_i in w]


def directional_variance(data: List[Vector], w: Vector) -> float:
    w_dir = direction(w)
    return sum(dot(vector, w_dir) ** 2 for vector in data)


def directional_variance_gradient(data: List[Vector], w: Vector) -> Vector:
    w_dir = direction(w)
    return [sum(2 * dot(vector, w_dir) * vector[i] for vector in data) for i in range(len(w))]


def first_principal_component(data: List[Vector], n: int = 100, step_size: float = 0.1) -> Vector:
    guess = [1.0 for _ in data[0]]

    with tqdm.trange(n) as t:
        for _ in t:
            dv = directional_variance(data, guess)
            gradient = directional_variance_gradient(data, guess)
            guess = gradient_step(guess, gradient, step_size)
            t.set_description(f"dv: {dv:.3f}")

    return direction(guess)


def project(v: Vector, w: Vector) -> Vector:
    projection_length = dot(v, w)
    return scalar_multiply(projection_length, w)


def remove_projection_from_vector(v: Vector, w: Vector) -> Vector:
    return subtract(v, project(v, w))


def remove_projection(data: List[Vector], w: Vector) -> List[Vector]:
    return [remove_projection_from_vector(v, w) for v in data]


def pca(data: List[Vector], num_components: int) -> List[Vector]:
    components: List[Vector] = []

    for _ in range(num_components):
        component = first_principal_component(data)
        components.append(component)
        data = remove_projection(data, component)

    return components


def transform_vector(v: Vector, components: List[Vector]) -> Vector:
    return [dot(v, w) for w in components]


def transform(data: List[Vector], components: List[Vector]) -> List[Vector]:
    return [transform_vector(v, components) for v in data]
