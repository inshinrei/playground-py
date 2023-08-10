import math


def min_operations(nums):
    ones = nums.count(1)
    n = len(nums)
    if ones > 0:
        return n - ones
    min_ops = math.inf
    for i, g in enumerate(nums):
        for j in range(i + 1, n):
            g = math.gcd(g, nums[j])
            if g == 1:
                min_ops = min(min_ops, j - i)
                break
    return -1 if min_ops == math.inf else min_ops + n - 1


assert min_operations([2, 6, 3, 4]) == 4
assert min_operations([2, 10, 6, 14]) == -1
