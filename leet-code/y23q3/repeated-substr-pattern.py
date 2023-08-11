def repeated_substr(s):
    return s in (s + s)[1:-1]


assert repeated_substr('abab') is True
assert repeated_substr('abcabcabcabc') is True
