"""
给定两个有序的向量S1和S2, 如何找出它们归并后所得的有序向量S的中位数

方法1: 暴力法, 将S1和S2归并为有序向量S, 然后直接取中位数, 时间效率为O(n1+n2), 适用于n1和n2较小的情况
方法2: 方法1没有充分利用两个子向量已经有序,
"""

# [lo1, lo1+n)   [lo2, lo2+n)
def trivia_median(nums1, lo1, n1, nums2, lo2, n2):
    hi1 = lo1 + n1
    hi2 = lo2 + n2
    nums = []

    while lo1 < hi1 and lo2 < hi2:
        while lo1 < hi1 and nums1[lo1] <= nums2[lo2]:
            nums.append(nums1[lo1])
            lo1 += 1
        while lo2 < hi2 and nums2[lo2] <= nums1[lo1]:
            nums.append(nums2[lo2])
            lo2 += 1

    while lo1 < hi1:
        nums.append(nums1[lo1])
        lo1 += 1

    while lo2 < hi2:
        nums.append(nums1[lo2])
        lo2 += 1

    return nums[(n1+n2) // 2]


def median(nums1, lo1, nums2, lo2, n):
    if n < 3:
        return trivia_median(nums1, lo1, n, nums2, lo2, n)

    mi1 = lo1 + n // 2
    mi2 = lo2 + (n-1) // 2
    if nums1[mi1] < nums2[mi2]:
        return median(nums1, mi1, nums2, lo2, n+lo1-mi1)
    elif nums1[mi1] < nums2[mi2]:
        return median(nums1, lo1, nums2, mi2, n+lo2-mi2)
    else:
        return nums1[mi1]


if __name__ == "__main__":
    nums1 = list(range(1, 20, 2))
    nums2 = list(range(0, 20, 2))
    print(nums1)
    print(nums2)

    print(trivia_median(nums1, 0, len(nums1), nums2, 0, len(nums2)))
    print(median(nums1, 0, nums2, 0, len(nums1)))