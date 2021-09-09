"""
寻找众数(存在某个元素的次数 > len(nums) / 2),
时间效率为O(n)

方法: 逐渐剪去前缀
"""


def majEleCandidate(nums):
    c = 0                       # 记录maj与其它元素的差额
    maj = nums[0]
    for i in range(len(nums)):
        if c == 0:              # 当c=0时, 前缀可以减除
            maj = nums[i]
            c = 1
        else:
            if maj == nums[i]:
                c += 1
            else:
                c -= 1
    return maj                  # 如果众数存在的话只可能是maj


def majEleCheck(nums, maj):
    occurrence = 0
    for e in nums:
        if e == maj:
            occurrence += 1

    return 2 * occurrence > len(nums)


def majority(nums):
    maj = majEleCandidate(nums)
    if majEleCheck(nums, maj):
        return maj
    else:
        return None

if __name__ == "__main__":
    nums = [1, 6, 8, 1, 9, 1, 2, 1, 1]
    nums1 = [2, 1, 6, 1, 8, 1, 9, 1, 2, 1, 1]
    nums2 = [1, 2, 3, 4, 5, 5, 6, 5, 1]
    print(majority(nums))
    print(majority(nums1))
    print(majority(nums2))
