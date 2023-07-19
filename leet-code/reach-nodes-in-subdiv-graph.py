from typing import List
import heapq
from collections import defaultdict


def reachable_nodes(edges: List[List[int]], max_moves: int, n: int) -> int:
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    min_heap = [(0, 0)]
    best = defaultdict(lambda: float('inf'))
    best[0] = 0
    count = defaultdict(lambda: defaultdict(int))
    result = 0
    while min_heap:
        curr_total, u = heapq.heappop(min_heap)  # O(|V|*log|V|) in total
        if best[u] < curr_total:
            continue
        result += 1
        for v, w in adj[u]:
            count[u][v] = min(w, max_moves - curr_total)
            next_total = curr_total + w + 1
            if next_total <= max_moves and next_total < best[v]:
                best[v] = next_total
                heapq.heappush(min_heap, (next_total, v))
    for u, v, w in edges:
        result += min(w, count[u][v] + count[v][u])
    return result


assert reachable_nodes([[0, 1, 10], [0, 2, 1], [1, 2, 2]], 6, 3) == 13
assert reachable_nodes([[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1]], 10, 4) == 23
assert reachable_nodes([[1, 2, 4], [1, 4, 5], [1, 3, 1], [2, 3, 4]], 17, 5) == 1
