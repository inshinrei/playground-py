def max_sum(nums, k):
    result = left = total = 0
    lookup = set()
    for r in range(len(nums)):
        while nums[r] in lookup or len(lookup) == k:
            lookup.remove(nums[left])
            total -= nums[left]
            left += 1
        lookup.add(nums[r])
        total += nums[r]
        if len(lookup) == k:
            result = max(result, total)
    return result


assert max_sum([1, 5, 4, 2, 9, 9, 9], 3) == 15
assert max_sum([4, 4, 4], 3) == 0
