"""
BST的中序遍历

    2
   / \
  1  3

中序遍历为: 1 -> 2 -> 3
"""


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.lchild = None
        self.rchild = None


def travel_in(root):
    if root is None:
        return
    travel_in(root.lchild)
    print(root.val)
    travel_in(root.rchild)


def go_along_left_branch(root, s):
    while root is not None:
        s.append(root)
        root = root.lchild
    return s


def travel_in_iteration(root):
    s = []
    x = root
    while True:
        s = go_along_left_branch(x, s)
        if len(s) == 0:
            break
        x = s.pop()
        print(x.val)
        x = x.rchild


def succ(root):
    if root.rchild is not None:
        node = root.rchild
        while node.lchild is not None:
            node = node.lchild
    else:
        # 找到最低左子树的祖先, 由于没有实现parent方法, 所以无法test
        while root.is_right_child():
            root = root.parent
        node = root.parent
    return node


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

    print("----------recursion----------")
    travel_in(bst_root)

    print("----------recursion----------")
    travel_in_iteration(bst_root)
