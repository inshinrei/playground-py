from typing import List


def max_sub(nums: List[int]) -> List[int]:
    max_sub = nums[0]
    curr_sum = 0
    for n in nums:
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += n
        max_sub = max(max_sub, curr_sum)
    return max_sub
