import re


def solve_equation(equation: str) -> str:
    no_solution = 'No solution'
    infinite_solutions = 'Infinite solutions'
    a, b, side = 0, 0, 1
    for eq, sign, num, isx in re.findall('(=)|([-+]?)(\d*)(x?)', equation):
        if eq:
            side = -1
        elif isx:
            a += side * int(sign + '1') * int(num or 1)
        elif num:
            b -= side * int(sign + num)
    if a:
        return 'x=%d' % (b / a)
    if b:
        return no_solution
    return infinite_solutions


assert solve_equation('x+5-3+x=6+x-2') == 'x=2'
assert solve_equation('x=x') == 'Infinite solutions'
assert solve_equation('2x=x') == 'x=0'
