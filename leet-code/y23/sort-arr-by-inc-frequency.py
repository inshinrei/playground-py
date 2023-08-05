from collections import Counter


def frequency_sort(nums):
    return sorted(nums, key=lambda n: (Counter(nums)[n], -n))


assert frequency_sort([1, 1, 2, 2, 2, 3]) == [3, 1, 1, 2, 2, 2]
assert frequency_sort([2, 3, 1, 3, 2]) == [1, 3, 3, 2, 2]
assert frequency_sort([-1, 1, -6, 4, 5, -6, 1, 4, 1]) == [5, -1, 4, 4, -6, -6, 1, 1, 1]
