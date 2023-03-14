with open('./input', 'r', encoding='utf-8') as input_data:
    data = input_data.read().splitlines()
    data = [r.split() for r in data]
    commands = [(r[0], int(r[1])) for r in data]
    h, d = 0, 0
    for c, v in commands:
        if c == 'forward':
            h += v
        elif c == 'down':
            d += v
        elif c == 'up':
            d -= v
        else:
            raise ValueError('Invalid command.')

    assert h * d == 1962940
