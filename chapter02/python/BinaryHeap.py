"""
如何建立堆:
1. 对空堆, 反复调用insert(O(logN)), 这样建堆的时间效率为O(NlogN), 不划算, 该时间足以给所有元素做全排序, 而堆里面还只是偏序
2. 对无序的堆, 反复调用swim, 时间效率同上
3. Floyd算法, 首先把所有无序的值存在堆里面, 然后自底向上进行sink, 这样每个元素最多sink一次, 所以时间效率为O(N)
"""


class MaxPQ:
    """
    最大二叉堆(也称优先级队列), 二叉堆其实就是完全二叉树, 但存在数组中, 把数组的索引当作指针
    最大二叉堆性质: 父节点 >= 左右节点
    插入和删除的时间复杂度为O(logN)
    """
    def __init__(self, nums=None):
        if nums is None:
            self.pq = [0]
            self.N = 0
        else:
            self.pq = [0] + nums
            self.N = len(nums)
            for i in range(self.N, 0, -1):
                self.sink(i)

    # 返回当前队列中最大的元素
    def max(self):
        return self.pq[1]

    # 插入元素e
    def insert(self, e):
        self.pq.append(e)
        self.N += 1
        self.swim(self.N)

    # 删除并返回当前队列中最大的元素
    def del_max(self):
        max_e = self.pq[1]
        tail = self.pq.pop()
        self.N -= 1
        self.pq[1] = tail
        self.sink(1)
        return max_e

    # 上浮第k个元素, 以维护最大二叉堆性质
    def swim(self, k):
        while k > 1 and self.pq[k] > self.pq[self.parent(k)]:
            self.exchange(k, self.parent(k))
            k = self.parent(k)

    # 下沉第k个元素, 以维护最大二叉堆性质
    def sink(self, k):
        while self.left(k) <= self.N:
            older = self.left(k)
            if self.right(k) <= self.N and self.pq[older] < self.pq[self.right(k)]:
                older = self.right(k)
            if self.pq[older] <= self.pq[k]:
                break

            self.exchange(k, older)
            k = older

    # 交换数组的两个元素
    def exchange(self, i, j):
        tmp = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = tmp

    def parent(self, root):
        return root // 2

    def left(self, root):
        return root * 2

    def right(self, root):
        return root * 2 + 1


if __name__ == "__main__":
    nums = [2, 5, 3, 7, 8, 1]
    bh = MaxPQ(nums)
    print(bh.pq)
