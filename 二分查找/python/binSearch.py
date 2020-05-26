class BinSearch:
    """
    该版本的停止条件为: left < right
    """

    @staticmethod
    def binSearch(nums, target):
        """
        二分查找, 碰到连续相等的元素会返回其中某个索引
        """
        if len(nums) == 0:
            return -1
        left = 0
        right = len(nums)

        # 搜索区间为[left, right), 停止条件为left = right + 1
        while left < right:
            mid = left + (right - left) // 2    # 这样写是防止left+right越界
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1                  # 很重要, 因为mid已经验证过了, 所以+1
            elif nums[mid] > target:
                right = mid

        return -1

    @staticmethod
    def left_bound(nums, target):
        """
        二分查找, 碰到连续相等的元素会返回最左边的索引, 首先找到数组中小于target的元素个数.
        在元素插入时很重要.
        """
        if len(nums) == 0:
            return -1
        left = 0
        right = len(nums)
        # 搜索区间为[left, right), 所以停止搜索的条件为left == right, 停止搜索时,
        # nums中有left个元素小于target
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] < target:
                # 搜索区间转为[mid+1, right), 因为mid已经验证过了, 所以+1
                left = mid + 1
            elif nums[mid] > target:
                # 搜索区间转为[left, mid), 因为mid不在搜索区间内, 所以right=mid就行
                right = mid

        # left=right的范围为[0, len(nums)]
        if left == len(nums) or nums[left] != target:
            return -1
        return left


    @staticmethod
    def right_bound(nums, target):
        if len(nums) == 0:
            return -1
        left = 0
        right = len(nums)
        # 搜索区间为[left, right), 停止时left == right, 停止搜索时, nums[right-1] >= target
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid

        # left=right的范围为[0, len(nums)]
        if right == 0 or nums[right - 1] != target:
            return -1
        return right - 1


if __name__ == '__main__':

    nums = [1, 2, 2, 2, 3, 3, 4, 4, 5, 6]
    targets = nums + [7, 0, 2.5]

    for target in targets:
        print(BinSearch.right_bound(nums, target))
