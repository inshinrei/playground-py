import numpy as np
from scipy import signal

with open('./input', 'r', encoding='utf-8') as input_data:
    data = input_data.read().splitlines()
    df = np.array([[int(x) for x in r] for r in data])
    total = 0
    for i in range(100):
        energy = np.ones_like(df)
        flashed = np.zeros_like(df)
        while np.any(energy.astype(bool)):
            df += energy
            flashing = np.logical_and((df > 9), np.logical_not(flashed))
            energy = signal.convolve(flashing, np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]]), mode='same')
            flashed = np.logical_or(flashed, flashing)
        df[flashed] = 0
        total += np.sum(flashed)
    print(total)
