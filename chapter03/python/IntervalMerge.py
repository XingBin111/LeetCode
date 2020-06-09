def interval_merge(nums):
    nums = sorted(nums, key=lambda x: x[0])
    res = []
    i = 1
    tmp = nums[0]
    while i < len(nums):
        if nums[i][0] < nums[i-1][1]:
            tmp = [tmp[0], nums[i][1]]
        else:
            res.append(tmp)
            tmp = nums[i]
        i += 1
    return res


if __name__ == "__main__":
    nums = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(interval_merge(nums))
