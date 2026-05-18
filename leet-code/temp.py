from typing import List


def produce_except_self(nums: List[int]) -> List[int]:
    pre = 1
    out = [1] * len(nums)
    for index in range(len(nums)):
        n = nums[index]

        out[index] = pre
        pre *= n

    post = 1
    for i in range(len(nums) - 1, -1, -1):
        v = nums[i]
        out[i] *= post
        post *= v
    return out
