from typing import List


# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}

    for i, value in enumerate(nums):
        remaining = target - nums[i]

        if remaining in seen:
            return [i, seen[remaining]]

        seen[value] = i


if __name__ == '__main__':

