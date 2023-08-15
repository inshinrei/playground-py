import heapq
import math


def find(n, _, time):
    result = 0
    left_bridge_q = [(-left_to_right - right_to_left, -i) for i, (left_to_right, pick_old, right_to_left, pick_new) in
                     enumerate(time)]
    right_bridge_q = []
    left_workers, right_workers = [], []
    heapq.heapify(left_bridge_q)
    while n > 0 or right_bridge_q or right_workers:
        while left_workers and left_workers[0][0] <= result:
            i = heapq.heappop(left_workers)[1]
            left_workers.pop()
            heapq.heappush(left_bridge_q, (-time[i][0] - time[i][2], -i))
        while right_workers and right_workers[0][0] <= result:
            i = heapq.heappop(right_workers)[1]
            heapq.heappush(right_bridge_q, (-time[i][0] - time[i][2], -i))
        if right_bridge_q:
            i = -heapq.heappop(right_bridge_q)[1]
            result += time[i][2]
            heapq.heappush(left_workers, (result + time[i][3], i))
        elif left_bridge_q and n > 0:
            i = -heapq.heappop(left_bridge_q)[1]
            result += time[i][0]
            heapq.heappush(right_workers, (result + time[i][1], i))
            n -= 1
        else:
            result = min(left_workers[0][0] if left_workers and n > 0 else math.inf,
                         right_workers[0][0] if right_workers else math.inf)
    return result


assert find(1, 3, [[1, 1, 2, 1], [1, 1, 3, 1], [1, 1, 4, 1]]) == 6
assert find(3, 2, [[1, 9, 1, 8], [10, 10, 10, 10]]) == 50
