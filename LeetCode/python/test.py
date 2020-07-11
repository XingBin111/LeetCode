class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        l = 0
        r = nums[-1] - nums[0]

        def isvalid(sum):
            cnt = 0
            l = 0
            for j, x in enumerate(nums):
                while x - nums[l] > sum:
                    l += 1
                cnt += j - l
                if cnt >= k:
                    return True
            return cnt >= k

        while r - l > 0:
            mid = (l + r) >> 1
            if isvalid(mid):
                r = mid
            else:
                l = mid + 1

        return r


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    s = Solution()
    print(s.smallestDistancePair(nums, 3))
