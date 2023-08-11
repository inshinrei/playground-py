def max_num(nums):
    nums.sort()
    left = 0
    for r in range((len(nums) + 1) // 2, len(nums)):
        if nums[r] >= 2 * nums[left]:
            left += 1
    return left * 2


assert max_num([3, 5, 2, 4]) == 2
assert max_num([9, 2, 5, 4]) == 4
assert max_num([7, 6, 8]) == 0
