def remove_sub(s: str) -> int:
    return 1 if s[::-1] == s else 2


assert remove_sub('ababa') == 1
assert remove_sub('abb') == 2
assert remove_sub('baabb') == 2
