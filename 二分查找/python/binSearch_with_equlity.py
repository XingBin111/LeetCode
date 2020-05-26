class BinSearch:
    """
    该版本的停止条件为: left <= right
    """

    @staticmethod
    def binSearch(nums, target):
        """
        二分查找, 碰到连续相等的元素会返回其中某个索引
        """
        left = 0
        right = len(nums) - 1

        # 很重要, 因为right=len(nums-1), 所以搜索区间为[left, right], 即使left=right, 区间还是有一个元素,
        # 还需要接着验证, 不用验证len(nums)==0的情况
        while left <= right:
            mid = left + (right - left) // 2    # 这样写是防止left+right越界
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1                  # 很重要, 因为mid已经验证过了, 所以+1
            elif nums[mid] > target:
                right = mid - 1                 # 很重要, 同理, 为了防止bug, 不使用else

        return -1

    @staticmethod
    def left_bound(nums, target):
        """
        二分查找, 碰到连续相等的元素会返回最左边的索引, 该版本在while中使用<=, 与最开始的binSearch保持一致
        """
        left = 0
        right = len(nums) - 1
        # 搜索区间为[left, right], 停止时left = right + 1, 停止搜索时, nums[left]
        # nums中有left个元素小于target
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] < target:
                # 搜索区间转为[mid+1, right], 因为mid已经验证过了, 所以+1
                left = mid + 1
            elif nums[mid] > target:
                # 搜索区间转为[left, mid-1], 因为mid已经验证过了, 所以-1
                right = mid - 1
        # left的范围为[0, len(nums)]
        if left == len(nums) or nums[left] != target:
            return -1
        return left

    @staticmethod
    def right_bound(nums, target):
        left = 0
        right = len(nums) - 1

        # 停止条件为left = right + 1, 停止时nums[right] >= target
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        # right的范围为[-1, len(nums)-1]
        if right == -1 or nums[right] != target:
            return -1
        return right


if __name__ == '__main__':

    nums = [1, 2, 2, 2, 3, 3, 4, 4, 5, 6]
    targets = nums + [7, 0, 2.5]

    for target in targets:
        print(BinSearch.right_bound(nums, target))
