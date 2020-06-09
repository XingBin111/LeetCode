"""
巧妙的对信封进行预处理, 然后就将问题变成了最长递归子序列问题(LIS). 666
预处理:
1. 对宽度进行升序排序
2. 对宽度相同的进行降序排序

[[5, 4], [6, 4], [6, 7], [2, 3]] ==> [[2, 3], [5, 4], [6, 7], [6, 4]]

这样做的话, 宽度相同信封的高度就不会出现在同一个LIS中.
"""

import functools


def tcmp(a, b):
    if a[0] > b[0]:
        return 1
    elif a[0] < b[0]:
        return -1
    else:
        if a[1] > b[1]:
            return -1
        else:
            return 1


def lis(heights):
    res = [heights[0]]
    piles = 1
    for i in range(1, len(heights)):
        h = heights[i]
        if h > res[-1]:
            piles += 1
            res.append(h)
        else:
            left = 0
            right = len(res)
            while left < right:
                mid = left + (right - left) // 2
                if res[mid] >= h:
                    right = mid
                else:
                    left = mid + 1

            res[right] = h
    return res


def envelopes(nums):
    sorted_nums = sorted(nums, key=functools.cmp_to_key(tcmp))
    height = [a[1] for a in sorted_nums]
    return len(lis(height))


if __name__ == "__main__":
    nums = [[5, 4], [6, 4], [6, 7], [2, 3]]
    print(envelopes(nums))
