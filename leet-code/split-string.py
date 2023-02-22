def split_string(string: str) -> bool:
    def backtrack(s: str, i: int, num: int, count: int) -> bool:
        if i == len(s):
            return count >= 2
        new_num = 0
        for j in range(i, len(s)):
            new_num = new_num * 10 + int(s[j])
            if new_num >= num >= 0:
                break
            if (num == -1 or num - 1 == new_num) and backtrack(s, j + 1, new_num, count + 1):
                return True
        return False
    return backtrack(string, 0, -1, 0)
