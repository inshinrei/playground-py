import re

with open('./input', 'r', encoding='utf-8') as input_data:
    data = input_data.read()
    coords_section, folds = data.split('\n\n')
    coords = {tuple(map(int, c.split(','))) for c in coords_section.splitlines()}
    folds = [re.match(r'fold along (x|y)=(\d+)', f).groups() for f in folds.splitlines()]
    folds = [(a, int(b)) for a, b in folds]
    for axis, v in folds[0:1]:
        if axis == 'y':
            coords = {(x, y) for x, y in coords if y < v} | {(x, v - (y - v)) for x, y in coords if y >= v}
        elif axis == 'x':
            coords = {(x, y) for x, y in coords if x < v} | {(v - (x - v), y) for x, y in coords if x >= v}
    assert len(coords) == 724
