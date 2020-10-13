"""
题目: 给定array, 每个元素都重复了2次, 除了某一个元素, 找到该元素并返回.
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
"""


class Solution:
    def singleNonDuplicate(self, nums):
        if len(nums) == 1:
            return nums[0]
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2

            if (mid % 2 == 0 and nums[mid] == nums[mid+1]) or (mid % 2 == 1 and nums[mid] == nums[mid-1]):
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]


if __name__ == "__main__":
    S = Solution()
    nums = [1,1,2]
    print(S.singleNonDuplicate(nums))


