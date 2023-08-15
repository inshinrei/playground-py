def find(word, m):
    result = []
    prev = 0
    for c in word:
        remainder = (prev * 10 + int(c)) % m
        result.append(1 if remainder == 0 else 0)
        prev = remainder
    return result


assert find('998244353', 3) == [1, 1, 0, 0, 0, 1, 1, 0, 0]
