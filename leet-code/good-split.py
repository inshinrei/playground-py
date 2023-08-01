def good_split_num(s):
    splits = 0
    n = len(s)
    prefix, suffix = [0] * n, [0] * n
    seen = set()
    for i in range(n):
        seen.add(s[i])
        prefix[i] = len(seen)
    seen.clear()
    for i in reversed(range(n)):
        seen.add(s[i])
        suffix[i] = len(seen)
    for i in range(n - 1):
        if prefix[i] == suffix[i + 1]:
            splits += 1
    return splits


assert good_split_num('aacaba') == 2
assert good_split_num('abcd') == 1
