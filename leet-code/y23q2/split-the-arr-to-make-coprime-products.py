from collections import Counter


def find_valid_split(nums):
    def factorize(n):
        result = []
        d = 2
        while d * d <= n:
            e = 0
            while n % d == 0:
                n //= d
                e += 1
            if e:
                result.append([d, e])
            d += 1 if d == 2 else 2
        if n > 1:
            result.append([n, 1])
        return result

    right = Counter()
    for x in reversed(nums):
        for p, c in factorize(x):
            right[p] += c
    left = Counter()
    cnt = 0
    for i in range(len(nums) - 1):
        for p, c in factorize(nums[i]):
            if not left[p]:
                cnt += 1
            left[p] += c
            right[p] -= c
            if not right[p]:
                cnt -= 1
        if not cnt:
            return i
    return -1


assert find_valid_split([4, 7, 8, 15, 3, 5]) == 2
assert find_valid_split([4, 7, 15, 8, 3, 5]) == -1
