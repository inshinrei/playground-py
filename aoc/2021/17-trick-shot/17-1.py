x1, x2, y1, y2 = 155, 215, -132, -72
best_y, count = 0, 0
for init_vx in range(1, x2 + 1):
    for init_vy in range(y1, 500):
        vx, vy = init_vx, init_vy
        x, y, max_y = 0, 0, y1
        while x <= 2 and y >= y1:
            max_y = max(max_y, y)
            if x1 <= x <= x2 and y1 <= y <= y2:
                count += 1
                best_y = max(best_y, max_y)
                break
            x += vx
            y += vy
            vx = max(0, vx - 1)
            vy -= 1
print(best_y)
