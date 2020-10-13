"""
题目: 假设一个升序的array在某个未知的pivot进行了旋转, 给定target, 如果target在array中返回True, 否则返回False
例子:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

searchI用于处理array不包含重复的元素, 因为无法处理nums[lo] == nums[mid] == nums[hi]
searchII可以处理重复元素
"""

class Solution:
    def searchI(self, nums, target) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid

            # 左边有序
            if nums[lo] <= nums[mid]:
                # 如果target在左边, 那么hi=mid-1
                if nums[lo] <= target <= nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            # 右边有序
            else:
                if nums[mid] <= nums[hi]:
                    if nums[mid] <= target <= nums[hi]:
                        lo = mid + 1
                    else:
                        hi = mid - 1
        return -1

    def searchII(self, nums, target) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid

            if nums[lo] == nums[mid] and nums[mid] == nums[hi]:
                hi -= 1
                lo += 1

            # 左边有序
            elif nums[lo] <= nums[mid]:
                # 如果target在左边, 那么hi=mid-1
                if nums[lo] <= target <= nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            # 右边有序
            else:
                if nums[mid] <= nums[hi]:
                    if nums[mid] <= target <= nums[hi]:
                        lo = mid + 1
                    else:
                        hi = mid - 1
        return -1


if __name__ == "__main__":
    S = Solution()
    nums = [1,3,1,1,1]
    print(S.search(nums, 3))
