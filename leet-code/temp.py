from typing import List


def third_max(nums: List[int]) -> int:
    fm, sm, tm = [None] * 3
    for n in nums:
        tfm = n == fm
        tsm = n == sm
        if tfm or tsm:
            continue
        if fm == None or n > fm:
            tm = sm
            sm = fm
            fm = n
        elif sm == None or n > sm:
            tm = sm
            sm = n
        elif tm == None or n > tm:
            tm = n

    if tm != None:
        return tm
    else:
        return fm


third_max([3, 2, 1])
