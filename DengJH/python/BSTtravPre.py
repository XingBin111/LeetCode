"""
BST的先序遍历

    2
   / \
  1  3

先序遍历为: 2 -> 1 -> 3
"""

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.lchild = None
        self.rchild = None


def travel_pre(root):
    if root is None:
        return
    print(root.val)
    travel_pre(root.lchild)
    travel_pre(root.rchild)


def travel_pre_iteration(root):
    s = [root]

    while len(s) > 0:
        node = s.pop()
        print(node.val)
        if node.rchild is not None:
            s.append(node.rchild)
        if node.lchild is not None:
            s.append(node.lchild)


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
    travel_pre(bst_root)

    print("----------recursion----------")
    travel_pre_iteration(bst_root)
