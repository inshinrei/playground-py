def get_knt(lo, hi, k):
    def get_power(n):
        if n == 1:
            return 0
        if n % 2 == 0:
            return 1 + get_power(n // 2)
        return 1 + get_power(n * 3 + 1)

    return sorted([(get_power(i), i) for i in range(lo, hi + 1)])[k - 1][1]


assert get_knt(12, 15, 2) == 13
assert get_knt(7, 11, 4) == 7
