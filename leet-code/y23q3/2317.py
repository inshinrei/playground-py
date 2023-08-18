from functools import reduce


def max_xor(nums):
    return reduce(lambda x, y: x | y, nums)
