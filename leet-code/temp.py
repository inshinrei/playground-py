import collections


def countStableSubarrays(capacity: list[int]) -> int:
    lookup = collections.Counter()
    buffer = collections.deque()
    count = 0
    current = 0

    for x in capacity:
        current += x
        count += lookup[(current - x * 2, x)]
        if len(buffer) > 0:
            lookup[buffer.popleft()] += 1
        buffer.append((current, x))
    return count
