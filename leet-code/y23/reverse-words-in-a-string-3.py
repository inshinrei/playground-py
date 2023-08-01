def reverse_words(s: str) -> str:
    return ' '.join([w[::-1] for w in s.split(' ')])


assert reverse_words("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
assert reverse_words("God Ding") == "doG gniD"
