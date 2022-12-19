from typing import Tuple, List

from liner_algebra.statistics import standard_deviation
from liner_algebra.vector import vectors_mean, Vector


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

    for vector in rescaled
        for i in range(dim):
            if stdevs[i] > 0:
                v[i] = (v[i] - means[i]) / stdevs[i]

    return rescaled
