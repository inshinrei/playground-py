from collections import Counter


def can_be_equal(target, arr):
    return Counter(target) == Counter(arr)
