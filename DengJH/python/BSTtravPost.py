"""
BST的后序遍历

    2
   / \
  1  3

后序遍历为: 1 -> 3 -> 2
"""


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.lchild = None
        self.rchild = None


def travel_post(root):
    if root is None:
        return

    travel_post(root.lchild)
    travel_post(root.rchild)
    print(root.val)


def gotoHLVFL(s):
    root = s[-1]
    while root is not None:
        if root.lchild is not None:
            if root.rchild is not None:
                s.append(root.rchild)
            s.append(root.lchild)
        elif root.rchild is not None:
            s.append(root.rchild)
        else:
            break
        root = s[-1]
    return s


def travel_post_iteration(root):
    x = root
    s = [x]
    while len(s) > 0:
        if s[-1] != x.parent:
            gotoHLVFL(s)
        x = s.pop()
        print(x.val)


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
    travel_post(bst_root)
