def longest(nums):
    result = 0
    cnt = 0
    l = 0
    for r, num in enumerate(nums):
        if num == 0:
            cnt += 1
        while cnt == 2:
            if nums[l] == 0:
                cnt -= 1
            l += 1
        result = max(result, r - l)
    return result


assert longest([1, 1, 0, 1]) == 3
assert longest([0, 1, 1, 1, 0, 1, 1, 0, 1]) == 5
