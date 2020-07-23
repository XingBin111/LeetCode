from DengJH.python.BSTtravIn import travel_in_iteration
from collections import deque

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.lchild = None
        self.rchild = None


class DFS:
    def serialize_deserialize_bt(self, root, s=""):
        if root is None:
            return "N"

        left = "," + self.serialize_deserialize_bt(root.lchild, s)
        right = "," + self.serialize_deserialize_bt(root.rchild, s)
        return str(root.val) + left + right

    def dfs_helper(self, q):
        val = q.popleft()

        if val == "N":
            return None

        root = TreeNode(int(val))
        root.lchild = self.dfs_helper(q)
        root.rchild = self.dfs_helper(q)
        return root

    # DFS
    def dfs_deserialize(self, s):
        l = s.split(",")
        q = deque()
        for e in l:
            q.append(e)
        root = self.dfs_helper(q)
        return root


# bfs更容易理解, 推荐使用
class BFS:
    def serialize_deserialize_bt(self, root):
        q = deque()
        q.append(root)
        res = []
        while len(q) > 0:
            node = q.popleft()
            if node is not None:
                res.append(node.val)
                q.append(node.lchild)
                q.append(node.rchild)
            else:
                res.append("N")
        return res

    def bfs_deserialize(self, l):
        q = deque()
        root = TreeNode(l[0])
        q.append(root)
        start = 1
        while start < len(l):
            node = q.popleft()
            first = l[start]
            second = l[start+1]

            if first != "N":
                node.lchild = TreeNode(first)
                q.append(node.lchild)
            else:
                node.lchild = None

            if second != "N":
                node.rchild = TreeNode(second)
                q.append(node.rchild)
            else:
                node.rchild = None
            start += 2
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

    print("--------------------------")
    dfs = DFS()
    s = dfs.serialize_deserialize_bt(bst_root)
    print(s)

    root = dfs.dfs_deserialize(s)
    travel_in_iteration(root)
    print("--------------------------")
    print("--------------------------")
    bfs = BFS()
    s = bfs.serialize_deserialize_bt(bst_root)
    print(s)
    bfs_root = bfs.bfs_deserialize(s)
    travel_in_iteration(bfs_root)
