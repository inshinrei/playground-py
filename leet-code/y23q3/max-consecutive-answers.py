from collections import Counter


def max_consecutive_answers(answer_key: str, k: int) -> int:
    result = max_count = 0
    count = Counter()
    for i in range(len(answer_key)):
        count[answer_key[i]] += 1
        max_count = max(max_count, count[answer_key[i]])
        if result - max_count >= k:
            count[answer_key[i - result]] -= 1
        else:
            result += 1
    return result


assert max_consecutive_answers('TTFF', 2) == 4
assert max_consecutive_answers('TFFT', 1) == 3
assert max_consecutive_answers('TTFTTFTT', 1) == 5
