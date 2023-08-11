from collections import defaultdict


def component_value(nums, edges):
    k_max = 1_000_000_000
    n = len(nums)
    _sum = sum(nums)
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    def dfs(u, target, seen):
        subtree_sum = nums[u]
        seen.add(u)
        for v in tree[u]:
            if v in seen:
                continue
            subtree_sum += dfs(v, target, seen)
            if subtree_sum > target:
                return k_max
        if subtree_sum == target:
            return 0
        return subtree_sum

    for i in range(n, 1, -1):
        if _sum % i == 0 and dfs(0, _sum // i, set()) == 0:
            return i - 1
    return 0


assert component_value([6, 2, 2, 2, 6], [[0, 1], [1, 2], [1, 3], [3, 4]]) == 2
assert component_value([2], []) == 0
