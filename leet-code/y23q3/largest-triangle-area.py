def largest(points):
    result = 0
    for Ax, Ay in points:
        for Bx, By in points:
            for Cx, Cy in points:
                result = max(result, 0.5 * abs((Bx - Ax) * (Cy - Ay) - (Cx - Ax) * (By - Ay)))
    return result


assert largest([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]) == 2.00000
assert largest([[1, 0], [0, 0], [0, 1]]) == 0.50000
