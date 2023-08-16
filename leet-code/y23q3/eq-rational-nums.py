def is_eq(s, t):
    ratios = [1, 1 / 9, 1 / 99, 1 / 999, 1 / 9999]

    def value_of(_s):
        if _s.find('(') == -1:
            return float(s)
        left_index = _s.find('(')
        right_index = _s.find(')')
        dot_index = _s.find('.')
        integer_and_not_repeating = float(s[:left_index])
        non_repeating_len = left_index - dot_index - 1
        repeating = int(s[left_index + 1:right_index])
        repeating_len = right_index - left_index - 1
        return integer_and_not_repeating + repeating * 0.1 ** non_repeating_len * ratios[repeating_len]

    return abs(value_of(s) - value_of(t)) < 1e-9
