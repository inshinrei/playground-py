import numpy as np

with open('./input', encoding='utf-8') as input_data:
    data = input_data.read()
    df = np.array([int(r) for r in data.split(',')])
    for day in range(80):
        df -= 1
        new = np.sum(df < 0)
        df = np.where(df < 0, 6, df)
        if new:
            df = np.hstack([df, np.full(new, 8)])
    print(str(df.shape).replace(',', ''))
