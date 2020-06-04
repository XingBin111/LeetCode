"""
使用栈实现队列, 队列实现栈
"""
from collections import deque


class MyQueue:
    """
    使用2个栈实现队列, 时间复杂度最坏为O(N), 因为可能将s1的元素都搬到s2中, 但均摊时间复杂度为O(1), 因为每个元素至多被搬一次
    """
    def __init__(self):
        self.s1 = []
        self.s2 = []

    # 添加元素到队尾
    def push(self, x):
        self.s1.append(x)

    # 删除队首元素, 并返回
    def pop(self):
        self.peek()
        return self.s2.pop()

    # 返回队首元素
    def peek(self):
        if len(self.s2) == 0:
            while len(self.s1) > 0:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    # 判断队列是否为空
    def empty(self):
        return len(self.s1) == 0 and len(self.s2) == 0


class MyStack:
    """
    使用一个队列实现栈, pop时间复杂度为O(N), 其他为O(1)
    """
    def __init__(self):
        self.q = deque([])
        self.top_elem = None

    def push(self, x):
        self.q.append(x)
        self.top_elem = x

    def pop(self):
        if self.empty():
            return None

        size = len(self.q)
        while size > 1:
            self.push(self.q.popleft())
            size -= 1
        return self.q.pop()

    def top(self):
        return self.top_elem

    def empty(self):
        return len(self.q) == 0
