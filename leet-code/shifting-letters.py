from typing import List


def shifting_letters_for(s: str, shifts: List[int]) -> str:
    result = []
    times = sum(shifts) % 26
    for i, c in enumerate(s):
        index = ord(c) - ord('a')
        result.append(chr(ord('a') + (index + times) % 26))
        times = (times - shifts[i]) % 26
    return ''.join(result)
