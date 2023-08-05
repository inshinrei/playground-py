def find_longest(s, d):
    result = ''
    for w in d:
        i = 0
        for c in s:
            if i < len(w) and c == w[i]:
                i += 1
        if i == len(w):
            if len(w) > len(result) or len(w) == len(result) and w < result:
                result = w
    return result


assert find_longest('abpcplea', ['ale', 'apple', 'monkey', 'plea'])
assert find_longest('abpcplea', ['a', 'b', 'c'])
