def merge(intervals):
    if len(intervals) == 0:
        return []
    s = sorted(intervals, key=lambda x: x[0])
    r = [s[0]]
    for i in s[1:]:
        if i[0] <= r[-1][1]:
            r[-1][1] = max(i[1], r[-1][1])
        else:
            r.append(i)
    return r


assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
assert merge([[1, 4], [4, 5]]) == [[1, 5]]
