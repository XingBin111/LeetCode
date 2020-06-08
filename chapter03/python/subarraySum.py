# 时间复杂度为O(n^2), 空间复杂度为O(n)
def subarraySum(nums, k):
    sum_table = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        sum_table[i+1] = sum_table[i] + nums[i]

    res = 0
    for i in range(1, len(nums)+1):
        for j in range(i):
            if sum_table[i] - sum_table[j] == k:
                res += 1
    return res


# 时间复杂度为O(n), 空间复杂度为O(n), 借助哈希表, 去除了不必要的嵌套
def subarraySumDict(nums, k):
    n = len(nums)
    d = {}
    d[0] = 1
    ans = 0
    sum0_i = 0

    for i in range(n):
        sum0_i += nums[i]
        sum0_j = sum0_i - k
        if sum0_j in d:
            ans += d.get(sum0_j)
        d[sum0_i] = d.get(sum0_i, 0) + 1
    return ans


if __name__ == "__main__":
    nums = [1, 1, 1]
    k = 2
    print(subarraySumDict(nums, k))
