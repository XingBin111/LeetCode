"""
寻找二叉树最低公共祖先
"""


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.lchild = None
        self.rchild = None


def backtrack(root, valA, valB):
    if root is None:
        return None
    if root.val == valA or root.val == valB:
        return root

    left = backtrack(root.lchild, valA, valB)
    right = backtrack(root.rchild, valA, valB)
    if left is not None and right is not None:
        return root
    elif right is not None:
        return right
    else:
        return left


def lca(root, valA, valB):
    return backtrack(root, valA, valB)


if __name__ == "__main__":
    bst_root = TreeNode(8)
    bst_root.lchild = TreeNode(0)
    bst_root.rchild = TreeNode(20)

    bst_root.lchild.lchild = TreeNode(-2)
    bst_root.lchild.rchild = TreeNode(4)
    bst_root.rchild.lchild = TreeNode(15)
    bst_root.rchild.rchild = TreeNode(30)

    bst_root.rchild.lchild.lchild = TreeNode(10)
    bst_root.rchild.lchild.rchild = TreeNode(16)
    bst_root.rchild.rchild.lchild = TreeNode(25)
    bst_root.rchild.rchild.rchild = TreeNode(35)

    node = lca(bst_root, 10, 35)
    print(node.val)
