def calc(s):
    result = 0
    prev, curr = 0, 0
    op = '+'
    for i, c in enumerate(s):
        if c.isdigit():
            curr = curr * 10 + int(c)
        if not c.isdigit() and c != ' ' or i == len(s) - 1:
            if op == '+' or op == '-':
                result += prev
                prev = (curr if op == '+' else -curr)
            elif op == '*':
                prev *= curr
            elif op == '/':
                prev = int(prev / curr)
            op = c
            curr = 0
    return result + prev


assert calc('3+2*2') == 7
assert calc('3/2') == 1
assert calc('3+5/2') == 5
