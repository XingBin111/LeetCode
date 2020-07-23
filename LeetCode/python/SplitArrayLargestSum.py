"""
给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。

给定nums = [7,2,5,10,8], m = 2, 有4种方法将nums分为2组, 而和最小的情况是[7,2,5] 和 [10,8]

思路: 和最小的值肯定属于[max(nums), sum(nums)], 所以使用二分查找
"""


def cal_split_times(nums, mid):
    res = 0
    s = 0
    i = 0
    while i < len(nums):
        if s + nums[i] <= mid:
            s += nums[i]
            i += 1
        else:
            s = 0
            res += 1
    if s > 0:
        res += 1
    return res


def split_array(nums, m):
    left = max(nums)
    right = sum(nums)
    while left <= right:
        mid = (left + right) // 2
        splits = cal_split_times(nums, mid)
        if splits <= m:
            right = mid - 1
        else:
            left = mid + 1
    return left


if __name__ == "__main__":
    nums = [7, 2, 5, 10, 8]
    m = 2
    print(split_array(nums, m))