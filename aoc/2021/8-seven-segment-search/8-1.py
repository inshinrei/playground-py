import numpy as np

with open('./input', 'r', encoding='utf-8') as input_data:
    data = input_data.read().splitlines()
    data = [r.split('|') for r in data]
    data = [(i.split(), o.split()) for i, o in data]
    total = 0
    for d in data:
        nb_segments = np.array([len(x) for x in d[1]])
        is1 = (nb_segments == 2).sum()
        is4 = (nb_segments == 4).sum()
        is7 = (nb_segments == 3).sum()
        is8 = (nb_segments == 7).sum()
        total += is1 + is4 + is7 + is8
    assert total == 416
