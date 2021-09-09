"""
核心思想: water[i] = min(左边最高的柱子, 右边最高的柱子) - heigh[i]
"""


# 时间复杂度O(N**2), l_max, r_max的计算方式很笨
def trap_brute(nums):
    n = len(nums)
    res = 0

    for i in range(1, n-1):
        l_max = 0
        r_max = 0

        for j in range(i+1, n):
            r_max = max(r_max, nums[j])

        for j in range(0, i):
            l_max = max(l_max, nums[j])

        if min(l_max, r_max) - nums[i] > 0:
            res += min(l_max, r_max) - nums[i]
    return res


# 时间复杂度O(N), 空间复杂度O(N), 预先将l_max, r_max计算出来, 计算方式比较巧妙
def trap_memo(nums):
    n = len(nums)
    res = 0

    l_max = nums.copy()
    r_max = nums.copy()

    for i in range(1, n-1):
        l_max[i] = max(l_max[i-1], nums[i])

    for i in range(n-2, 0, -1):
        r_max[i] = max(r_max[i+1], nums[i])

    for i in range(1, n-1):
        res += max(0, min(l_max[i], r_max[i]) - nums[i])
    return res


# 时间复杂度O(N), 空间复杂度O(1), 从两端往中间计算, 很巧妙
def trap_double_pointer(nums):
    n = len(nums)
    res = 0

    left = 0
    right = n - 1
    l_max = nums[0]
    r_max = nums[-1]

    while left <= right:
        if l_max > r_max:
            res += max(r_max - nums[right], 0)
            right -= 1
            r_max = max(r_max, nums[right])
        else:
            res += max(l_max - nums[left], 0)
            left += 1
            l_max = max(l_max, nums[left])
    return res


if __name__ == "__main__":
    nums = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trap_brute(nums))
    print(trap_memo(nums))
    print(trap_double_pointer(nums))
