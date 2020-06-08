"""
对于无序的数组只能穷举, 暴力穷举的时间复杂度为O(N^2), 可借助HashMap, 以空间换时间, 因为HashMap的查询为O(1)
"""


def two_sum(nums, target):
    # 时间复杂度O(N), 空间复杂度O(N)
    d = {}
    for i, e in enumerate(nums):
        d[e] = i

    for i, e in enumerate(nums):
        k = target - e
        if k in d and d[k] != i:
            return i, d[k]
    return -1, -1


if __name__ == "__main__":
    nums = [3, 1, 3, 6]
    target = 6
    print(two_sum(nums, target))
