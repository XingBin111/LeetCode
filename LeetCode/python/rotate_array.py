class Solution:
    def rotate(self, nums: [int], k: int) -> None:
        n = len(nums)
        k %= n

        start = count = 0
        while count < n:
            cur_idx, prev = start, nums[start]
            while True:
                next_idx = (cur_idx + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                cur_idx = next_idx
                count += 1

                if start == cur_idx:
                    break
            start += 1


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    k = 2
    s = Solution()
    s.rotate(nums, k)
    print(nums)
