"""
对于这种数组问题，关键点在于元素和索引是成对儿出现的，常用的方法是排序、异或、映射。
映射的思路就是我们刚才的分析，将每个索引和元素映射起来，通过正负号记录某个元素是否被映射。
"""


def find_error_eums(nums):
    n = len(nums)
    dup = -1
    for i in range(n):
        idx = abs(nums[i]) - 1
        if nums[idx] < 0:
            dup = abs(nums[i])
        else:
            nums[idx] *= -1

    missing = -1
    for i in range(n):
        if nums[i] > 0:
            missing = i + 1
    return [dup, missing]


if __name__ == "__main__":
    nums = [4, 1, 4, 2]
    print(find_error_eums(nums))
