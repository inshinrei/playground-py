import math


def stickers_to_spell(stickers, target):
    n = len(target)
    max_mask = 1 << n
    dp = [math.inf] * max_mask
    dp[0] = 0
    for mask in range(max_mask):
        if dp[mask] == math.inf:
            continue
        for s in stickers:
            _mask = mask
            for c in s:
                for i, t in enumerate(target):
                    if c == t and not (_mask >> i & 1):
                        _mask |= 1 << i
                        break
            dp[_mask] = min(dp[_mask], dp[mask] + 1)
    return -1 if dp[-1] == math.inf else dp[-1]


assert stickers_to_spell(['with', 'example', 'science'], 'thehat') == 3
assert stickers_to_spell(['notice', 'possible'], 'basicbasic') == -1
