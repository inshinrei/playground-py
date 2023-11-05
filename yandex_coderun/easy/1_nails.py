def solve(count, nails):
    assert count == len(nails), 'Insufficient nails len'
    a = [0] * 101
    dp = [0] * 101
    for i in range(count):
        a[i] = nails[i]
    a = sorted(a[1:count])
    dp[2] = a[2] - a[1]
    dp[3] = a[3] - a[1]
    for i in range(4, count):
        dp[i] = min(dp[i - 1], dp[i - 2] + a[i] - a[i - 1])
    return dp[count]


assert solve(6, [3, 13, 12, 4, 14, 6]) == 5
