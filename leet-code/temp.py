from typing import List


def test(nums: List[int]) -> List[int]:
    res = max(nums)
    curr_min, curr_max = 1, 1
    for n in nums:
        tmp_max = n * curr_max
        curr_max = max(n * curr_max, n * curr_min, n)
        curr_min = min(tmp_max, n * curr_min, n)
        res = max(res, curr_max, curr_min)
    return res
