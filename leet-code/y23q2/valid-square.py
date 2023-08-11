def valid_square(p1, p2, p3, p4) -> bool:
    def distance(p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    lookup = {distance(p1, p2), distance(p1, p3), distance(p1, p4), distance(p2, p3), distance(p2, p4),
              distance(p3, p4)}
    return 0 not in lookup and len(lookup) == 2


assert valid_square([0, 0], [1, 1], [1, 0], [0, 1]) is True
assert valid_square([0, 0], [1, 1], [1, 0], [0, 12]) is False
assert valid_square([1, 0], [-1, 0], [0, 1], [0, -1]) is True
