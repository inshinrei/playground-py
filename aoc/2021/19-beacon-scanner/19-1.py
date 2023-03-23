from collections import Counter

scanners = []
with open('./input', 'r', encoding='utf-8') as input_data:
    data = [s for s in input_data.read().split('\n\n')]
    for r in data:
        scanner = [[int(d) for d in line.strip().split(',')] for line in r.splitlines()[1:]]
        scanners.append(scanner)


def check(_scanners, base, to_check):
    offsets, orientation = [], []
    base_scanner = _scanners[base]
    scanner_to_check = _scanners[to_check]
    for i in range(3):
        for sign, d in [(1, 0), (-1, 0), (1, 1), (-1, 1), (1, 2), (-1, 2)]:
            diffs = [beacon0[i] - sign * beacon1[d] for beacon1 in scanner_to_check for beacon0 in base_scanner]
            offset, matching = Counter(diffs).most_common()[0]
            if matching >= 12:
                offsets.append(offset)
                orientation.append((sign, d))
    return offsets, orientation


def find_overlapping(_scanner, to_check):
    for s in to_check:
        offsets, orientation = check(scanners, _scanner, s)
        if len(offsets) > 0:
            return s, offsets, orientation
    return -1, [], []


def align_scanner_globally(_scanner, offsets, orientation):
    to_align = scanners[_scanner]
    sign0, col0 = orientation[0]
    sign1, col1 = orientation[1]
    sign2, col2 = orientation[2]
    to_align = [[sign0 * beacon[col0], sign1 * beacon[col1], sign2 * beacon[col2]] for beacon in to_align]
    to_align = [[beacon[0] + offsets[0], beacon[1] + offsets[1], beacon[2] + offsets[2]] for beacon in to_align]
    scanners[_scanner] = to_align


def align_scanners(_scanners):
    aligned = [0]
    unaligned = [i for i in range(1, len(_scanners))]
    offsets = []
    while unaligned:
        for i in aligned:
            overlapping, offset, orientation = find_overlapping(i, unaligned)
            if overlapping != -1:
                align_scanner_globally(overlapping, offset, orientation)
                unaligned.remove(overlapping)
                aligned.append(overlapping)
                offsets.append(offset)
    return offsets


def count(_scanners):
    unique = set()
    for s in _scanners:
        for beacon in s:
            unique.add((beacon[0], beacon[1], beacon[2]))
    return len(unique)


def get_distance(offsets):
    d = 0
    for i in range(len(offsets)):
        for j in range(i + 1, len(offsets)):
            m = abs(offsets[i][0] - offsets[j][0]) + abs(offsets[i][1] - offsets[j][1]) + abs(
                offsets[i][2] - offsets[j][2])
            d = max(d, m)
    return d
