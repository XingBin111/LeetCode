"""
给定一个正整数，实现一个方法来求出离该整数最近的大于自身的“换位数”。
什么是换位数呢？就是把一个整数各个数位的数字进行全排列，从而得到新的整数。

输入12345，返回12354
输入12354，返回12435
输入12435，返回12453

思路:
1.从后向前查看逆序区域，找到逆序区域的前一位，也就是数字置换的边界

2.把逆序区域的前一位和逆序区域中刚刚大于它的数字交换位置

3.把原来的逆序区域转为顺序
"""


def findNearestNumber(nums):
    n = len(nums)

    # 1.
    for i in range(n-1, 0, -1):
        if nums[i-1] < nums[i]:
            break

    if i == 0:
        return None

    gap = 10
    k = i
    for j in range(i, n):
        if nums[j] - nums[i-1] < gap:
            gap = nums[j] - nums[i-1]
            k = j
    # 2.
    nums[i-1], nums[k] = nums[k], nums[i-1]

    # 3.
    nums[i:] = sorted(nums[i:])
    return nums


if __name__ == "__main__":
    nums = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 5, 4],
        [1, 2, 4, 3, 5],
    ]
    for e in nums:
        print(findNearestNumber(e))
