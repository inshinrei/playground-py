def contains_pattern(arr, m, k):
    if len(arr) < m * k:
        return False
    i = 0
    iterate_len = m * k
    while i + iterate_len <= len(arr):
        t = arr[i:i + iterate_len]
        if t[:m] * k == t:
            return True
        i += 1
    return False


assert contains_pattern([1, 2, 4, 4, 4, 4], 1, 3) is True
assert contains_pattern([1, 2, 1, 2, 1, 1, 1, 3], 2, 2) is True
assert contains_pattern([1, 2, 1, 2, 1, 3], 2, 3) is False
