def count(ranges):
    _mod = 10 ** 9 + 7
    ranges.sort()
    c = 0
    current = float('-inf')
    for l, r in ranges:
        if l > current:
            c += 1
        current = max(current, r)
    return pow(2, c, _mod)


assert count([[6, 10], [5, 15]]) == 2
assert count([[1, 3], [10, 20], [2, 5], [4, 8]]) == 4
