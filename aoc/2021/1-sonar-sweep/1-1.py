with open('./input', 'r', encoding='utf-8') as input_data:
    data = input_data.read().splitlines()
    depths = [int(r) for r in data]
    increases = sum(x < y for x, y in zip(depths, depths[1:]))
    print(increases)
