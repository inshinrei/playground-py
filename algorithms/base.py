def bead_sort(seq: list) -> list:
    if any(not isinstance(x, int) or x < 0 for x in seq):
        raise TypeError("Sequence must be list of non-negative integers")
    for _ in range(len(seq)):
        for i, (rod_upper, rod_lower) in enumerate(zip(seq, seq[1:])):
            if rod_upper > rod_lower:
                seq[i] -= rod_upper - rod_lower
                seq[i+1] += rod_upper - rod_lower
    return seq