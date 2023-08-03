class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def balance_bst(root):
    nums = []

    def inorder(_root):
        if not _root:
            return None
        inorder(_root.left)
        nums.append(_root.val)
        inorder(_root.right)

    inorder(root)

    def build(l, r):
        if l > r:
            return None
        m = (l + r) // 2
        return TreeNode(nums[m], build(l, m - 1), build(m + 1, r))

    return build(0, len(nums) - 1)
