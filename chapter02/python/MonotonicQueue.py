"""
时间复杂度O(n), 空间复杂度O(k), 虽然push中有while, 但每个元素至多pop和push一次, 所以时间复杂度为O(n)
"""

from collections import deque


class MontionicQueue:
    def __init__(self):
        self.deque = deque([])

    # 队尾添加元素
    def push(self, n):
        while len(self.deque) > 0 and self.deque[-1] < n:
            self.deque.pop()
        self.deque.append(n)

    # 返回当前队列中最大元素
    def max(self):
        return self.deque[0]

    # 如果队首元素是n, 就删除它
    def pop(self, n):
        if len(self.deque) > 0 and self.deque[0] == n:
            self.deque.popleft()


def max_slinding_window(nums, k):
    dq = MontionicQueue()
    res = []
    for i in range(len(nums)):
        if i < k - 1:
            dq.push(nums[i])
        else:
            dq.push(nums[i])
            res.append(dq.max())
            dq.pop(nums[i - k + 1])
    return res


if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(max_slinding_window(nums, k))
