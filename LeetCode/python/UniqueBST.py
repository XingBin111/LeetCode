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

    res = s.generateTrees(2)
    for r in res:
        print(r.val)