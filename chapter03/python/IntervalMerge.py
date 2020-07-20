def interval_merge(nums):
    nums = sorted(nums, key=lambda x: x[0])
    res = [nums[0]]
    for i in range(1, len(nums)):
        cur = nums[i]
        if cur[0] < res[-1][1]:
            res[-1][1] = cur[1]
        else:
            res.append(nums[i])
    return res


if __name__ == "__main__":
    nums = [[1, 3], [2, 6], [5, 7], [8, 10], [15, 18]]
    print(interval_merge(nums))