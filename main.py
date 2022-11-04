"""
Given a binary tree, determine if it is
height-balanced

Input: root = [3,9,20,null,null,15,7]
Output: true
"""


if __name__ == '__main__':
    def isBalanced(self, root) -> bool:
        if root is None:
            return True

        def dfs(node):
            if node is None:
                return 0
            return max(dfs(root.left), dfs(root.right)) + 1

        return abs(
            dfs(root.left) - dfs(root.right)
        ) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
