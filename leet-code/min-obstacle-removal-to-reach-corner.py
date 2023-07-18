from typing import List


def min_obstacles(grid: List[List[int]]) -> int:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def move(g, b, t):
        f, dh = 0, 1
        closer, detour = [b], []
        lookup = set()
        while closer or detour:
            if not closer:
                f += dh
                closer, detour = detour, closer
            b = closer.pop()
            if b in lookup:
                continue
            lookup.add(b)
            if b == t:
                return f
            for dr, dc in directions:
                nb = (b[0] + dr, b[1] + dc)
                if not (0 <= nb[0] < len(g) and 0 <= nb[1] < len(g[0]) and nb not in lookup):
                    continue
                (closer if not g[b[0]][b[1]] else detour).append(nb)
        return -1

    return move(grid, (0, 0), (len(grid) - 1, len(grid[0]) - 1))


assert min_obstacles([[0, 1, 1], [1, 1, 0], [1, 1, 0]]) == 2
assert min_obstacles([[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]]) == 0
