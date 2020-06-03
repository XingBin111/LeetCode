def next_greater_element(nums):
    res = nums.copy()
    stack = []
    for i in range(len(res) - 1, -1, -1):
        while len(stack) > 0 and stack[-1] <= nums[i]:
            stack.pop()
        res[i] = -1 if len(stack) == 0 else stack[-1]
        stack.append(nums[i])
    return res


# 假设数组是个环形，可以将idx加倍, 用的时候取idx = idx % len(nums)
def next_greater_element_circle(nums):
    n = len(nums)
    res = nums.copy()
    stack = []
    for i in range(2 * n - 1, -1, -1):
        while len(stack) > 0 and stack[-1] <= nums[i % n]:
            stack.pop()
        res[i % n] = -1 if len(stack) == 0 else stack[-1]
        stack.append(nums[i % n])
    return res


def next_greater_element_idx(nums):
    res = list(range(len(nums)))
    stack = []
    for i in range(len(res) - 1, -1, -1):
        while len(stack) > 0 and nums[stack[-1]] <= nums[i]:
            stack.pop()
        res[i] = -1 if len(stack) == 0 else stack[-1]
        stack.append(i)
    return res


if __name__ == "__main__":
    nums = [2, 1, 2, 4, 3]
    print(next_greater_element_circle(nums))
