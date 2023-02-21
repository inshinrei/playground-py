from typing import List


def shift_letter(c: str, times) -> str:
    index = ord(c) - ord('a')
    return chr(ord('a') + (index + times) % 26)


def shifting_letters_for(s: str, shifts: List[int]) -> str:
    result = []
    times = sum(shifts) % 26
    for i, c in enumerate(s):
        result.append(shift_letter(c, times))
        times = (times - shifts[i]) % 26
    return ''.join(result)
