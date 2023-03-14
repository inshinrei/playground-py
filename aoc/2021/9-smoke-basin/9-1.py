import numpy as np

with open('./input', 'r', encoding='utf-8') as input_data:
    data = input_data.read()
    df = np.array([list(map(int, [r for r in line])) for line in data.splitlines()])
    pad = np.pad(df, ((1, 1), (1, 1)), 'constant', constant_values=10)
    mask = (
            (df < pad[1:-1, 0:-2]).astype(int) +
            (df < pad[1:-1, 2:]).astype(int) +
            (df < pad[0:-2, 1:-1]).astype(int) +
            (df < pad[2:, 1:-1]).astype(int)
    )
    assert (df + 1)[mask == 4].sum() == 550
