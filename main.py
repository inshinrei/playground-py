"""

"""


if __name__ == '__main__':
    def is_power_of_four(n: int) -> bool:
        current_pick = 4
        while current_pick <= n:
            if current_pick == n:
                return True
            current_pick *= 4
        return False

    print(is_power_of_four(16))
