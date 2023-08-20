def tree(t):
    def dfs(root):
        if not root:
            return ''
        if root.right:
            return str(root.val) + '(' + dfs(root.left) + ')(' + dfs(root.right) + ')'
        if root.left:
            return str(root.val) + '(' + dfs(root.left) + ')'
        return str(root.val)

    return dfs(t)
