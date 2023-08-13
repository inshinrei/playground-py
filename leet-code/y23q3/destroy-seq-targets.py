from collections import Counter


def destroy(nums, space):
    cnt = Counter([num % space for num in nums])
    max_cnt = max(cnt.values())
    return min(num for num in nums if cnt[num % space] == max_cnt)


assert destroy([1, 3, 5, 2, 4, 7], 2) == 1
assert destroy([6, 2, 5], 100) == 2
