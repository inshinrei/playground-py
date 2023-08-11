def find_longest(s, dict):
    result = ''
    for word in dict:
        i = 0
        for c in s:
            if i < len(word) and c == word[i]:
                i += 1
        if i == len(word):
            if len(word) > len(result) or len(word) == len(result) and word < result:
                result = word
    return result


assert find_longest('abpcplea', ['ale', 'apple', 'monkey', 'plea'])
assert find_longest('abpcplea', ['a', 'b', 'c'])
