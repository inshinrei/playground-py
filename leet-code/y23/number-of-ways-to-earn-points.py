def ways_to_reach_target(target, types):
    k_mod = 1_000_000_007  # int(1e9 + 7)
    dp = [1] + [0] * target
    for count, mark in types:
        for j in range(target, -1, -1):
            for solved in range(1, count + 1):
                if j - solved * mark >= 0:
                    dp[j] += dp[j - solved * mark]
                    dp[j] %= k_mod
    return dp[target]


assert ways_to_reach_target(6, [[6, 1], [3, 2], [2, 3]]) == 7
assert ways_to_reach_target(5, [[50, 1], [50, 2], [50, 5]]) == 4
