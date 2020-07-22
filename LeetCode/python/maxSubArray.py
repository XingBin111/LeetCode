"""
连续子数组的最大和
"""

def maxSubArray(nums):
    cur_sum = 0
    max_sum = nums[0]
    for e in nums:
        if cur_sum >= 0:
            cur_sum += e
        else:
            cur_sum = e
        if cur_sum > max_sum:
            max_sum = cur_sum
    return max_sum


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxSubArray(nums))