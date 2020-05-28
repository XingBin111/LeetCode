"""
给出几堆石头, 两个人比赛拿石头, 每次只能拿最左边或最右边的的石头堆, 求max(先手拿-后手拿)
"""

import numpy as np


def stone_game(nums):
    if len(nums) == 1:
        return nums[0]
    dp_table = np.zeros((len(nums), len(nums)), dtype=np.int32)
    for i in range(len(nums)):
        dp_table[i, i] = nums[i]

    for i in range(len(nums)-1, -1, -1):
        for j in range(i+1, len(nums)):
            dp_table[i, j] = max(nums[i]-dp_table[i+1, j], nums[j]-dp_table[i, j-1])
    return dp_table[0, -1]


if __name__ == "__main__":
    nums = [3, 9, 1, 2]
    print(stone_game(nums))
