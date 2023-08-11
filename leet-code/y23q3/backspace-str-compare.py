def compare(s, t):
    i = len(s) - 1
    j = len(t) - 1
    while True:
        backspace = 0
        while i >= 0 and (s[i] == '#' or backspace > 0):
            backspace += 1 if s[i] == '#' else -1
            i -= 1
        backspace = 0
        while j >= 0 and (t[j] == '#' or backspace > 0):
            backspace += 1 if t[j] == '#' else -1
            j -= 1
        if i >= 0 and j >= 0 and s[i] == t[j]:
            i -= 1
            j -= 1
        else:
            break
    return i == -1 and j == -1


assert compare('ab#c', 'ad#c') is True
assert compare('ab##', 'c#d#') is True
assert compare('a#c', 'b') is False
