def total(nums):
    dp = [0] * len(nums)
    stack = []
    for i, n in enumerate(nums):
        step = 1
        while stack and nums[stack[-1]] <= n:
            step = max(step, dp[stack.pop()] + 1)
        if stack:
            dp[i] = step
        stack.append(i)
    return max(dp)
