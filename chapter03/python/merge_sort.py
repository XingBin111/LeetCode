class MergeSort:
    def __init__(self):
        self.nums = None

    def merge(self, nums, lo, mid, hi):
        i = lo
        j = mid + 1
        for k in range(lo, hi + 1):
            self.nums[k] = nums[k]

        for k in range(lo, hi + 1):
            if i > mid:
                nums[k] = self.nums[j]
                j += 1
            elif j > hi:
                nums[k] = self.nums[i]
                i += 1

            elif self.nums[i] > self.nums[j]:
                nums[k] = self.nums[j]
                j += 1
            else:
                nums[k] = self.nums[i]
                i += 1

    def _merge_sort(self, nums, lo, hi):
        if lo >= hi:
            return
        mid = (lo + hi) // 2
        self._merge_sort(nums, lo, mid)
        self._merge_sort(nums, mid + 1, hi)
        self.merge(nums, lo, mid, hi)

    def merge_sort(self, nums):
        self.nums = [0] * len(nums)
        self._merge_sort(nums, 0, len(nums) - 1)
        return nums


if __name__ == "__main__":
    nums = [3, 6, 1, 9, 7, 2, 4]
    ms = MergeSort()
    new_nums = ms.merge_sort(nums)
    print(new_nums)

