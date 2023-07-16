from collections import deque


def reverse_words(s: str) -> str:
    d = deque()
    result = ''
    for c in s.strip():
        if c == ' ':
            result += ''.join(d) + ' '
            d.clear()
            continue
        d.appendleft(c)
    if d:
        result += ''.join(d)
        d.clear()
    return result.strip()


assert reverse_words("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
assert reverse_words("God Ding") == "doG gniD"
