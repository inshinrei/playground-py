from typing import List


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
