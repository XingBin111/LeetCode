class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.lchild = None
        self.rchild = None

    def is_leaf(self):
        return self.lchild is None and self.rchild is None


def plus_one(root):
    if root is None:
        return
    root.val += 1
    plus_one(root.lchild)
    plus_one(root.rchild)


# 先序遍历
def show_tree(root):
    if root is None:
        return
    print(root.val)
    show_tree(root.lchild)
    show_tree(root.rchild)


def is_same_tree(root1, root2):
    if root1 is None:
        return root2 is None
    if root2 is None:
        return root1 is None

    if root1.val != root2.val:
        return False

    return is_same_tree(root1.lchild, root2.lchild) and is_same_tree(root1.rchild, root2.rchild)


# 666
def is_valid_bin_search_tree(root, min=None, max=None):
    if root is None:
        return True

    if min is not None and min.val > root.val:
        return False

    if max is not None and max.val < root.val:
        return False

    return is_valid_bin_search_tree(root.lchild, min, root) and is_valid_bin_search_tree(root.rchild, root, max)


def is_in_bst(root, target):
    if root is None:
        return False

    if root.val == target:
        return True

    if target > root.val:
        return is_in_bst(root.rchild, target)
    else:
        return is_in_bst(root.lchild, target)


# 默认target不在树中, 注意要return root
def insert_in_bst(root, target):
    if root is None:
        return TreeNode(target)

    if target > root.val:
        root.rchild = insert_in_bst(root.rchild, target)
    else:
        root.lchild = insert_in_bst(root.lchild, target)
    return root


def bst_get_min(root):
    while root.lchild is not None:
        root = root.lchild
    return root


# 情况1: node.val=target的节点是叶节点, 那么直接令 node = None
# 情况2: node.val=target的节点无左孩子, 那么直接令 node = node.rchild, 无右节点, 就直接令 node = node.lchild
# 情况3: node.val=target的节点有左右孩子, 直接令 node = 左子树中最大或右子树最小, 下面代码是取右子树最小
def delete_taget_in_bst(root, target):
    if root is None:
        return None

    if root.val == target:
        if root.lchild is None:
            return root.rchild
        if root.rchild is None:
            return root.lchild

        x = bst_get_min(root.rchild)
        root.val = x.val
        root.rchild = delete_taget_in_bst(root.rchild, x.val)

    elif target > root.val:
        root.rchild = delete_taget_in_bst(root.rchild, target)
    else:
        root.lchild = delete_taget_in_bst(root.lchild, target)
    return root


if __name__ == "__main__":
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
    # plus_one(root)
    # print("tree of root:")
    # show_tree(root)

    # print(is_valid_bin_search_tree(root))

    # print("tree of root1:")
    # show_tree(root1)
    # print(is_same_tree(root, root1))

    bst_root = TreeNode(8)
    bst_root.lchild = TreeNode(4)
    bst_root.rchild = TreeNode(10)

    bst_root.lchild.rchild = TreeNode(6)
    bst_root.rchild.lchild = TreeNode(9)
    bst_root.rchild.rchild = TreeNode(11)
    # print(is_valid_bin_search_tree(bst_root))

    # print(is_in_bst(bst_root, 3))
    # print(is_in_bst(bst_root, 9))
    # insert_in_bst(bst_root, 3)
    show_tree(bst_root)
    print("delete:")
    delete_taget_in_bst(bst_root, 10)
    show_tree(bst_root)