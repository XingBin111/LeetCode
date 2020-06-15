"""
洗牌算法: 将长度为n的数组乱序, 即打乱的可能性有n!种排列结果
分析洗牌算法正确性的准则：产生的结果必须有 n! 种可能，否则就是错误的
"""


import random


def random_int(a, b):
    # 返回[a, b]范围内任意整数
    return random.uniform(a, b)


def swap(nums, i, j):
    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp


def shuffleI(nums):
    n = len(nums)
    for i in range(n):
        r = random_int(i, n-1)
        swap(nums, i, r)


def shuffleII(nums):
    n = len(nums)
    for i in range(n-1):
        r = random_int(i, n - 1)
        swap(nums, i, r)


def shuffleIII(nums):
    n = len(nums)
    for i in range(n-1, -1, -1):
        r = random_int(0, i)
        swap(nums, i, r)


def shuffleIIII(nums):
    n = len(nums)
    for i in range(n-1, 0):
        r = random_int(0, i)
        swap(nums, i, r)


# 该方法得到的结果有n^n种可能, 所以不属于洗牌算法
def shuffle_wrong(nums):
    n = len(nums)
    for i in range(n-1, 0):
        r = random_int(0, n-1)
        swap(nums, i, r)