from math import log

"""

"""


if __name__ == '__main__':
    def is_power_of_four(n: int) -> bool:
        if n <= 0:
            return False

        return (log(n) / log(4)).is_integer()

    print(is_power_of_four(16))
