res = []


# 时间复杂度为O(n^2), 递归深度为n, 每次递归要花费O(n)来创建列表
# 该方法计算出的操作并以一定是最优操作
def pancakeSort(nums, sorted_nums):
    n = len(nums)
    if n == 1:
        return
    idx = nums.index(sorted_nums[n-1])
    if idx == 0:
        pancakeSort(nums[1:][::-1], sorted_nums[:-1])
        res.append(n)
    elif idx == n - 1:
        pancakeSort(nums[:-1], sorted_nums[:-1])
    else:
        new_nums = nums[idx+1: n][::-1] + nums[:idx]
        new_sorted_nums = sorted_nums[:-1]
        res.append(idx+1)
        res.append(n)
        pancakeSort(new_nums, new_sorted_nums)


if __name__ == "__main__":
    nums = [3, 2, 4, 1]
    sorted_nums = sorted(nums)
    pancakeSort(nums, sorted_nums)
    print(res)