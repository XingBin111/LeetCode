"""
BST递归套路

void BST(root, target):
    if root == None:
        return TreeNode(target)
    if target > root.val:
        root.rchild = BST(root.rchild, target)
    else:
        root.lchild = BST(root.lchild, target)
    return root
"""


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.lchild = None
        self.rchild = None

    def is_leaf(self):
        return self.lchild is None and self.rchild is None


def isValidBST(root, min_val=None, max_val=None):
    if root is None:
        return True

    if min_val is not None and root.val < min_val.val:
        return False

    if max_val is not None and root.val > max_val.val:
        return False

    return isValidBST(root.lchild, min_val, root) and isValidBST(root.rchild, root, max_val)


def insert(root, val):
    if root is None:
        return TreeNode(val)

    if val > root.val:
        root.rchild = insert(root.rchild, val)
    else:
        root.lchild = insert(root.lchild, val)
    return root


def show_tree(root):
    if root is None:
        return
    show_tree(root.lchild)
    print(root.val)
    show_tree(root.rchild)


def getMin(root):
    while root.lchild is not None:
        root = root.lchild
    return root


def delete(root, val):
    if root is None:
        return None
    if val > root.val:
        root.rchild = delete(root.rchild, val)
    elif val == root.val:
        if root.lchild is None:
            return root.rchild
        elif root.rchild is None:
            return root.lchild
        else:
            node = getMin(root)
            root.val = node.val
            root.rchild = delete(root.rchild, node.val)
    else:
        root.lchild = delete(root.lchild, val)
    return root


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

    root = TreeNode(3)
    root.lchild = TreeNode(4)
    root.rchild = TreeNode(5)

    root.lchild.rchild = TreeNode(6)
    root.rchild.lchild = TreeNode(7)

    root1 = TreeNode(3)
    root1.lchild = TreeNode(4)
    root1.rchild = TreeNode(5)

    root1.lchild.lchild = TreeNode(1)
    root1.lchild.rchild = TreeNode(6)
    root1.rchild.lchild = TreeNode(7)

    # print(isValidBST(bst_root))
    # print(isValidBST(root))

    # bst_root = insert(bst_root, 2)

    bst_root = delete(bst_root, 20)
    show_tree(bst_root)

