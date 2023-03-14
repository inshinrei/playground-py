import numpy as np

with open('./input.txt', encoding='utf-8') as input_data:
    data = input_data.read().splitlines()
    data = [r.replace(' -> ', ',').split(',') for r in data]
    data = [list(map(int, r)) for r in data]
    size = max(max(r) for r in data) + 1
    diagram = np.zeros((size, size), dtype=int)
    for x1, y1, x2, y2 in data:
        x1, y1, x2, y2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
        if x1 == x2 or y1 == y2:
            diagram[y1: y2 + 1, x1: x2 + 1] += 1
    assert np.sum(diagram > 1) == 6283
