"""
输入nums, k, t, 判断是否存在 abs(num[i]-nums[j]) <= t 且 abs(i-j) <= k
使用一个长度为k的滑动窗口, 窗口内元素是有序的, 对待添加到窗口的元素进行abs(num[i]-nums[j]) <= t
时间复杂度为O(nk)
"""

from sortedcontainers import SortedList
from bisect import bisect_left, bisect_right


def containsNearbyAlmostDuplicate(nums, k, t):
    SList = SortedList()
    for i in range(len(nums)):
        if i > k:
            SList.remove(nums[i - k - 1])
        
        # 使用二分查找
        pos1 = bisect_left(SList, nums[i] - t)
        pos2 = bisect_right(SList, nums[i] + t)

        # 原作者的代码为pos1 != pos2 and pos1 != len(SList), 但改为下面也可以通过 
        if pos1 != pos2:
            return True

        # O(k)
        SList.add(nums[i])

    return False


if __name__ == "__main__":
    nums = [1, 5, 9, 1, 5, 9]
    k = 2
    t = 3

    print(containsNearbyAlmostDuplicate(nums, k, t))
