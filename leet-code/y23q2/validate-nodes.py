def validate_nodes(n, left, right):
    queue = []
    size = 0
    visited = set()
    nodes = set(left + right)
    for x in range(n):
        if x not in nodes:
            queue.append(x)
            break
    else:
        queue.append(0)
    while queue:
        i = queue.pop(0)
        if i != -1 and i not in visited:
            size += 1
            visited.add(i)
            queue.append(left[i])
            queue.append(right[i])
        elif i == -1:
            continue
        else:
            return False
    return size == n


assert validate_nodes(4, [1, -1, 3, -1], [2, -1, -1, -1]) is True
assert validate_nodes(4, [1, -1, 3, -1], [2, 3, -1, -1]) is False
