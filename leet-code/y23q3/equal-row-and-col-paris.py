from typing import List
from collections import Counter


def equal_paris(grid: List[List[int]]) -> int:
    cnt_1 = Counter(tuple(r) for r in grid)
    cnt_2 = Counter(tuple(c) for c in zip(*grid))
    return sum(cnt_1[k] * cnt_2[k] for k in cnt_1.keys() if k in cnt_2)


assert equal_paris([[3, 2, 1], [1, 7, 6], [2, 7, 7]]) == 1
assert equal_paris([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]) == 3
