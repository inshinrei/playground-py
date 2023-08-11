def min_moves(seats, students):
    return sum(abs(seat - student) for seat, student in zip(sorted(seats), sorted(students)))


assert min_moves([3, 1, 5], [2, 7, 4]) == 4
assert min_moves([4, 1, 5, 9], [1, 3, 2, 6]) == 7
