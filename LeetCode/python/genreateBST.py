"""
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树
"""



class TreeNode:
    def __init__(self, val=0, lchild=None, rchild=None):
        self.val = val
        self.lchild = lchild
        self.rchild = rchild


def generate(start, end):
    res = []

    for i in range(start, end+1):
        left = generate(start, i-1)
        right = generate(i+1, end)

        for j in left:
            for k in right:
                node = TreeNode(i, j, k)
                res.append(node)
    if len(res) == 0:
        res.append(None)
    return res


def generateBST(n):
    return generate(1, n)


if __name__ == "__main__":
    n = 3
    res = generateBST(n)
    print(res)
