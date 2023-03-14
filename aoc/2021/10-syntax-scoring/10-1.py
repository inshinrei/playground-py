def count_points(line: str) -> int:
    s = []
    for c in line:
        if c in '([{<':
            s.append(c)
        elif c in ')':
            if s.pop() != '(':
                return 3
        elif c in ']':
            if s.pop() != '[':
                return 57
        elif c in '}':
            if s.pop() != '{':
                return 1197
        elif c in '>':
            if s.pop() != '<':
                return 25137
    return 0


with open('./input', 'r', encoding='utf-8') as input_data:
    data = input_data.read().splitlines()
    assert sum(count_points(r) for r in data) == 299793
