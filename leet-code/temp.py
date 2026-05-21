from typing import List


def test(nums: List[int]) -> List[int]:
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid
        if nums[mid] >= nums[l]:
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        else:
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    return -1
