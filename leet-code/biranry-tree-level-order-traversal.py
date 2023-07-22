class TreeNode:
    def __int__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    if root is None:
        return []
    result, current = [], [root]
    while current:
        next_level, vals = [], []
        for node in current:
            vals.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        current = next_level
        result.append(vals)
    return result

# assert level_order([3, 9, 20, None, None, 15, 7]) == [[3], [9, 20], [15, 7]]
# assert level_order([1]) == [[1]]
# assert level_order([]) == []
