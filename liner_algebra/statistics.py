from collections import Counter
from typing import List, Tuple
from liner_algebra.probability import normal_cdf, inverse_normal_cdf

import math


def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)


def _median_odd(xs: List[float]) -> float:
    return sorted(xs)[len(xs) // 2]


def _median_even(xs: List[float]) -> float:
    sorted_xs = sorted(xs)
    high_midpoint = len(xs) // 2
    return (sorted_xs[high_midpoint - 1] + sorted_xs[high_midpoint]) / 2


def median(v: List[float]) -> float:
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)


assert median([1, 10, 2, 9, 5]) == 5
assert median([1, 9, 2, 10]) == (2 + 9) / 2


def quantile(xs: List[float], p: float) -> float:
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]


def mode(x: List[float]) -> List[float]:
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]


def data_range(xs: List[float]) -> float:
    return max(xs) - min(xs)


def de_mean(xs: List[float]) -> List[float]:
    x_bar = mean(xs)
    return [x - x_bar for x in xs]


def variance(xs: List[float]) -> float:
    from liner_algebra.vector import sum_of_squares

    assert len(xs) >= 2, 'variance requires at least two elems'

    n = len(xs)
    deviations = de_mean(xs)
    return sum_of_squares(deviations) / (n - 1)


def standard_deviation(xs: List[float]) -> float:
    return math.sqrt(variance(xs))


def interquartile_range(xs: List[float]) -> float:
    return quantile(xs, 0.75 - quantile(xs, 0.25))


def covariance(xs: List[float], ys: List[float]) -> float:
    from liner_algebra.vector import dot

    assert len(xs) == len(ys), 'must be the same length'

    return dot(de_mean(xs), de_mean(ys)) / (len(xs) - 1)


def correlation(xs: List[float], ys: List[float]) -> float:
    xs_standard_deviation = standard_deviation(xs)
    ys_standard_deviation = standard_deviation(ys)

    if (xs_standard_deviation > 0 and ys_standard_deviation > 0):
        return covariance(xs, ys) / xs_standard_deviation / ys_standard_deviation
    else:
        return 0


def normal_approximation_to_binomial(n: int, p: float) -> Tuple[float, float]:
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma


def normal_probability_above(low: float, mu: float = 0, sigma: float = 1) -> float:
    return 1 - normal_cdf(low, mu, sigma)


def normal_probability_between(low: float, high: float, mu: float = 0, sigma: float = 1) -> float:
    return normal_cdf(high, mu, sigma) - normal_cdf(low, mu, sigma)


def normal_probability_outside(low: float, high: float, mu: float = 0, sigma: float = 1) -> float:
    return 1 - normal_probability_between(low, high, mu, sigma)

