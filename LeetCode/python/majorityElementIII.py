"""
对于一个整数序列, 找到出现次数超过三分之一的元素. 与众数的思想很类似.

例如: nums = [3, 2, 3], return [3]
例如: nums = [1, 2], return [1, 2]
"""

class Solution:
    def majorityElement(self, nums):
        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [n for n in (candidate1, candidate2)
                if nums.count(n) > len(nums) // 3]


if __name__ == "__main__":
    nums = [3, 2, 3]
    S = Solution()
    print(S.majorityElement(nums))
