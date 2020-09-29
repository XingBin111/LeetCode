from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        res = 0
        q = deque()
        q.append(root)
        while q:
            res = 0
            for i in range(len(q)):
                root = q.popleft()
                res += root.val
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
        return res


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.right = TreeNode(6)
    root.right.right.right = TreeNode(8)

    root.left.left.left = TreeNode(4)

    s = Solution()

    print(s.deepestLeavesSum(root))
