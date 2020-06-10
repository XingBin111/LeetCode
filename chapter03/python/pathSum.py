class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


# pathSumI会找到不连续的路径, 例如:10 -> -2, 所以行不通, 要保证, 一旦pathSumI(root.left, target - root.val), 则root.left后续每个节点都要减去val
def path_sum_bad(root, target):
    if root is None:
        return 0

    if target == root.val:
        return 1

    res = 0
    res += path_sum_bad(root.left, target)

    res += path_sum_bad(root.left, target - root.val)

    res += path_sum_bad(root.right, target)

    res += path_sum_bad(root.right, target - root.val)

    return res


def count(root, target):
    if root is None:
        return 0
    return (root.val == target) + count(root.left, target-root.val) + count(root.right, target-root.val)


def path_sum_good(root, target):
    if root is None:
        return 0
    return count(root, target) + count(root.left, target) + count(root.right, target)


if __name__ == "__main__":
    target = 8

    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(-3)

    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    root.right.right = TreeNode(11)

    root.left.left.left = TreeNode(-1)
    root.left.left.right = TreeNode(-2)
    root.left.right.right = TreeNode(1)

    print(path_sum_good(root, target))

