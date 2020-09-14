"""
给定n, 返回所有存储1~n的BST.

这道题的解题依据依然是：
当数组为 1，2，3，4，.. i，.. n时，基于以下原则的BST建树具有唯一性：
以i为根节点的树，其左子树由[1, i-1]构成， 其右子树由[i+1, n]构成。 
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.lchild = left
        self.rchild = right

    def is_leaf(self):
        return self.lchild is None and self.rchild is None


class Solution:

    def generateTrees(self, n: int) -> [TreeNode]:

        # EDGE CASE
        if n == 0:
            return []

        # CALL ON  BUILD() TO RETURN THE LIST OF ROOTS
        return self.build(1, n)

    def build(self, start, end):
        trees = []

        # CHOOSE A ROOT VALUE ANYWHERE BETWEEN [START, END]
        for val in range(start, end + 1):

            # ATTACH ROOT TO EVERY POSSIBLE LEFT SUBTREE
            for left in self.build(start, val - 1):

                # ATTACH ROOT TO EVERY POSSIBLE RIGHT SUBTREE
                for right in self.build(val + 1, end):
                    # CREATE A TREE AND ADD IT
                    trees.append(TreeNode(val, left, right))

        # [NONE] = THE EMPTY TREE
        return trees or [None]


if __name__ == "__main__":
    s = Solution()

    res = s.generateTrees(3)
    print(res)
    for r in res:
        print(r.val)
