def second_greater(nums):
    result = [-1] * len(nums)
    prev = []
    curr = []
    for i, num in enumerate(nums):
        while prev and nums[prev[-1]] < num:
            result[prev.pop()] = num
        decreasing_indices = []
        while curr and nums[curr[-1]] < num:
            decreasing_indices.append(curr.pop())
        while decreasing_indices:
            prev.append(decreasing_indices.pop())
        curr.append(i)
    return result


assert second_greater([2, 4, 0, 9, 6]) == [9, 6, 6, -1, -1]
assert second_greater([3, 3]) == [-1, -1]
