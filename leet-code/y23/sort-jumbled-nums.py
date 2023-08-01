def sort_jumbled(mapping, nums):
    def get_mapped(num):
        m = []
        for c in str(num):
            m.append(str(mapping[ord(c) - ord('0')]))
        return int(''.join(m))

    A = [(get_mapped(n), i, n) for i, n in enumerate(nums)]
    return [num for _, i, num in sorted(A)]


assert sort_jumbled([8, 9, 4, 0, 2, 1, 3, 5, 7, 6], [991, 338, 38]) == [338, 38, 991]
