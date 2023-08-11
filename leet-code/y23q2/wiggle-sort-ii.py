def wiggle_sort(nums):
    size = len(nums)
    nums.sort()
    mid_i = (size - 1) // 2
    nums[::2], nums[1::2] = nums[mid_i::-1], nums[:mid_i:-1]


assert wiggle_sort([1, 5, 1, 1, 6, 4]) == [1, 6, 1, 5, 1, 4]
assert wiggle_sort([1, 3, 2, 2, 3, 1]) == [2, 3, 1, 3, 1, 2]
