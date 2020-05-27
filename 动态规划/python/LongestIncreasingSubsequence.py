def LSI(nums):
    """
    寻找nums中最常递增子序列， 复杂度为O(N^2)
    """
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def lengthOfLIS(nums):
    top = [0] * len(nums)
    piles = 0
    for i in range(len(nums)):
        left = 0
        right = piles
        while left < right:
            mid = (right + left) // 2
            if top[mid] < nums[i]:
                left = mid + 1
            elif nums[mid] > nums[i]:
                right = mid
            else:
                left = mid + 1
        if right == piles:
            piles += 1
        top[piles] = nums[i]
    return piles


nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(lengthOfLIS(nums))
