def count(n):
    def dfs(entries, i, memo):
        if i > memo:
            return 1
        result = 0
        for c in entries:
            if c % i == 0 or i % c == 0:
                entries.remove(c)
                result += dfs(entries, i + 1, memo)
                entries.add(c)
        return result

    return dfs(set(range(1, n + 1)), 1, n)
