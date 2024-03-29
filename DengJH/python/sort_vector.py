"""
快排的平均效率为O(n*logn), 比较其它的排序算法, 它的时间复杂度的常系数更小, 具体为O(2*ln2*log_2(n))=O(1.386log_2(n))
"""

import random


def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]


# 搜索区间为[lo, hi]
# 不稳定, 数值相同的元素, 在排序后可能不能保持原始次序
def partitionI(nums, lo, hi):
    random_idx = random.randint(lo, hi-1)
    # print("lo={}, hi={}, random_idx={}".format(lo, hi, random_idx))
    swap(nums, lo, random_idx)
    pivot = nums[lo]
    while lo < hi:
        while lo < hi and pivot <= nums[hi]:
            hi -= 1
        nums[lo] = nums[hi]

        while lo < hi and pivot >= nums[lo]:
            lo += 1
        nums[hi] = nums[lo]
    nums[lo] = pivot
    return lo


# L = [lo, mi], G = [mi+1, k-1], U = [k, hi]
# 不稳定, 数值相同的元素, 在排序后可能不能保持原始次序
def partitionII(nums, lo, hi):
    random_idx = random.randint(lo, hi-1)
    swap(nums, lo, random_idx)
    pivot = nums[lo]
    mi = lo
    for k in range(lo+1, hi+1):
        if nums[k] < pivot:
            swap(nums, mi+1, k)
            mi += 1
    swap(nums, lo, mi)
    return mi


# 若每次划分平均(轴点的选取都接近中央), 时间效率为O(nlogn), 若每次划分都极不平均(轴点总是最大或最小元素), 时间效率为O(n^2)
# 但平均性能为O(nlogn), 搜索区间为[lo, hi)
def quick_sort(nums, lo=0, hi=1):
    if hi - lo < 2:
        return

    # mi已经排序好了
    mi = partitionII(nums, lo, hi-1)

    # 排序[lo, mi)
    quick_sort(nums, lo, mi)

    # 排序[mi+1, hi)
    quick_sort(nums, mi+1, hi)


def bubble_sort(nums):
    n = len(nums)
    sort = True
    for i in range(n):
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                sort = False
        if sort:
            break
        else:
            sort = True


def select_sort(nums):
    n = len(nums)
    for i in range(n-1):
        min_idx = nums[i]
        for j in range(i+1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j

        nums[min_idx], nums[i] = nums[i], nums[min_idx]


def merge_sort(nums):
    pass


def insert_sort(nums):
    pass


if __name__ == "__main__":
    nums = [6, 3, 8, 2, 5, 9, 4, 5, 1, 7]
    quick_sort(nums, 0, len(nums))
    # select_sort(nums)
    print(nums)

