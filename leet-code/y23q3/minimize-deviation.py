import heapq
from typing import List


def minimize_deviation(nums: List[int]) -> int:
    heap = [-num * 2 if num % 2 else -num for num in nums]
    heapq.heapify(heap)
    min_elem = -max(heap)
    result = float('inf')
    while len(heap) == len(nums):
        num = -heapq.heappop(heap)
        result = min(result, num - min_elem)
        if not num % 2:
            min_elem = min(min_elem, num // 2)
            heapq.heappush(heap, -num // 2)
    return result


assert minimize_deviation([1, 2, 3, 4]) == 1
assert minimize_deviation([4, 1, 5, 20, 3]) == 3
assert minimize_deviation([2, 10, 8]) == 3
