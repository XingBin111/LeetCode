"""
rob1: 每个房内都藏有一定的先进, 但不能偷窃两件相邻的房屋, 每个房屋存放非负整数的金币, 求能够偷窃到的最高金额
rob2: 新增条件: 房子围成了一个圈, 也就是第一间和最后一间相邻
rob3: 房子在一颗二插树上, 例如[3, 2, 3, null, 3, null, 1], 最大金额=3+3+1=7

        3
    /       \
  2          3
  \            \
    3           1
"""


class TreeNode:
    def __init__(self, val=0, parent=None, left=None, right=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right


def rob1(nums):
    if len(nums) <= 2:
        return max(nums)
    dp = nums
    for i in range(2, len(nums)):
        # 状态转移分2种情况:
        #   1. i-1被偷了, 所以没法偷i
        #   2. i-2被偷了, 所以可以偷i
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    return max(dp)


def rob1_optimized(nums):
    if len(nums) <= 2:
        return max(nums)
    dp_i_0 = nums[0]
    dp_i_1 = nums[1]
    dp_i = 0
    for i in range(2, len(nums)):
        # 由于dp[i]只与前2个状态有关, 所以可以优化空间效率
        dp_i = max(dp_i_1, dp_i_0 + nums[i])
        dp_i_0 = dp_i_1
        dp_i_1 = dp_i
    return dp_i


def rob2(nums):
    """
    可退化到rob1:
    1. 去掉第一间房
    2. 去掉最后一间
    3. 同时去掉第一间和最后一间(1和2选择范围比3多, 金币是非负, 所以可以不用讨论这种情况)
    """
    n = len(nums)
    if n <= 2:
        return 0

    return max(
        rob1_optimized(nums[0:n - 1]),
        rob1_optimized(nums[1:n]),
    )


def rob3(root):
    d = {}
    def rob(root):
        if root == None:
            return 0
        if root in d:
            return d[root]
        if root.left is not None:
            left_left = rob(root.left.left)
            left_right = rob(root.left.right)
            left_val = root.left.val
        else:
            left_left = 0
            left_right = 0
            left_val = 0

        if root.right is not None:
            right_left = rob(root.right.left)
            right_right = rob(root.right.right)
            right_val = root.right.val
        else:
            right_left = 0
            right_right = 0
            right_val = 0
        rob_root = root.val + left_left + left_right + right_left + right_right
        no_rob_root = left_val + right_val
        d[root] = max(rob_root, no_rob_root)
        return d[root]
    return rob(root)


if __name__ == "__main__":
    nums = [2, 7, 9, 3, 1]
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.right = TreeNode(3)
    root.right.right = TreeNode(1)

    print(rob3(root))
