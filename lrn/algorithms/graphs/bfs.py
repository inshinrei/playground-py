def is_valid(img, row, col):
    return 0 <= row < len(img) and 0 <= col < len(img[0])


def neighbors(img, row, col, start):
    indices = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    return [(row, col) for row, col in indices if is_valid(img, row, col) and img[row][col] == start]


def flood_fill(img, row, col, p):
    start = img[row][col]
    queue = [(row, col)]
    visited = set()
    while len(queue) > 0:
        row, col = queue.pop(0)
        visited.add((row, col))
        img[row][col] = p
        for row, col in neighbors(img, row, col, start):
            if (row, col) not in visited:
                queue.append((row, col))
    return img
