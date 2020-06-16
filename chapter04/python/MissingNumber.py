

# 异或运算总是能够消除成对的元素
# 异或运算: 当两对应的二进位相异时，结果为1
# 满足性质: x^x = 0, x^0 = x, x^y^x=y^(x^x)=y^0=y
def missing_numberI(nums):
    n = len(nums)
    res = 0
    res ^= n

    for i in range(n):
        res ^= i ^ nums[i]
    return res


def missing_numberII(nums):
    n = len(nums)
    s = n * (n + 1) // 2
    return s - sum(nums)


# 为避免s溢出
def missing_numberIII(nums):
    n = len(nums)
    res = n
    for i in range(n):
        res += i - nums[i]
    return res


if __name__ == "__main__":
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(missing_numberI(nums))
    print(missing_numberII(nums))
    print(missing_numberIII(nums))
