def nth_num(n, primes):
    k = len(primes)
    nums = [1]
    indices = [0] * k
    while len(nums) < n:
        _next = [0] * k
        for i in range(k):
            _next[i] = nums[indices[i]] * primes[i]
        next_num = min(_next)
        for i in range(k):
            if next_num == _next[i]:
                indices[i] += 1
        nums.append(next_num)
    return nums[-1]


assert nth_num(12, [2, 7, 13, 19])
assert nth_num(1, [2, 3, 5])
