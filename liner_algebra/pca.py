from typing import Tuple, List

from liner_algebra.statistics import standard_deviation
from liner_algebra.vector import vectors_mean, Vector


def scale(data: List[Vector]) -> Tuple[Vector, Vector]:
    dim = len(data[0])

    means = vectors_mean(data)
    stdevs = [standard_deviation([vector[i] for vector in data]) for i in range(dim)]

    return means, stdevs