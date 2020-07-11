"""
找到节点p， q在root中的最低公共祖先
"""

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def lowestCommonAncestor(root, p, q):
    if root == p or root == q or root is None:
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if left is not None and right is not None:
        return root

    return left if left is not None else right


if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(-3)

    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    root.right.right = TreeNode(11)

    root.left.left.left = TreeNode(-1)
    root.left.left.right = TreeNode(-2)
    root.left.right.right = TreeNode(1)

    r = lowestCommonAncestor(root, root.left.left.left, root.left.right)
    print(r.val)
