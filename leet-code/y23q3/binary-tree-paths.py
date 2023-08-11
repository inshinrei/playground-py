def paths(root):
    res = []

    def dfs(_root, path):
        if not _root:
            return
        if not _root.left and not _root.right:
            res.append(''.join(path) + str(_root.val))
            return
        path.append(str(_root.val) + '->')
        dfs(_root.left, path)
        dfs(_root.right, path)
        path.pop()

    dfs(root, [])
    return res
