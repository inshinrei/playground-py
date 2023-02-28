with open('./input', encoding='utf-8') as input_data:
    data = input_data.read()
    df = list(map(int, data.split(',')))
    p_min, p_max = min(df), max(df)
    fuels = [sum(map(lambda x: abs(x - p), df)) for p in range(p_min, p_max + 1)]
    print(min(fuels))
