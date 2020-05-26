class LeftRightPointer:

    @staticmethod
    def two_num_sum(nums, target):
        """
        给定一个升序排列的数组nums, 找到数组中两个数使得它们的和等于target
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return [left, right]
            elif nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
        return [-1, -1]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 10
    print(LeftRightPointer.two_num_sum(nums, target))