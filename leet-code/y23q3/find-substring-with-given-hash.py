def sub_string_hash(s, power, modulo, k, hash):
    h, index = 0, -1
    pw = pow(power, k - 1, modulo)
    for i in reversed(range(len(s))):
        if i + k < len(s):
            h = (h - (ord(s[i + k]) - ord('a') + 1) * pw) % modulo
        h = (h * power + (ord(s[i]) - ord('a') + 1)) % modulo
        if h == hash:
            index = i
    return s[index:index + k]


assert sub_string_hash('fbxzaad', 31, 100, 3, 32)
