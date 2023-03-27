import numpy as np
from scipy.signal import convolve2d


def enhance(times):
    with open('./input', 'r', encoding='utf-8') as input_data:
        data = input_data.read().splitlines()
        algo = [int(x == '#') for x in data[0]]
        img = np.array([[int(x == '#') for x in y] for y in data[2:]])
        matrix = np.array([[1, 2, 4], [8, 16, 32], [64, 128, 256]])
        fill_value = 0
        for _ in range(times):
            index = convolve2d(img, matrix, fillvalue=fill_value)
            img = np.vectorize(lambda x: algo[x])(index)
            fill_value = algo[0] if fill_value == 0 else algo[511]
        return img.sum()


assert enhance(2) == 5249
