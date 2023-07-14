from collections import Counter


def count_sub_arrays(nums, k):
    index = nums.index(k)
    lookup = Counter()
    current = 0
    for i in reversed(range(index + 1)):
        current += 0 if nums[i] == k else -1 if nums[i] < k else +1
        lookup[str(current)] += 1
    result = current = 0
    for i in range(index, len(nums)):
        current += 0 if nums[i] == k else -1 if nums[i] < k else +1
        result += lookup[str(-current)] + lookup[str(-(current - 1))]
    return result


assert count_sub_arrays([2, 3, 1], 3) == 1
assert count_sub_arrays([3, 2, 1, 4, 5], 4) == 3
