"""
优先级队列:普通队列是按照入栈的时间顺序出栈, 而优先级队列是按照优先级顺序来出栈, 通常用于任务调度, 给紧急的任务更高的优先级

使用python内置的最小堆来实现优先级队列
"""

import heapq


def smallest_queue_test(arr):
    """
    默认为最小优先队列
    """
    print("原数组：{0}".format(arr))
    # 将给定的列表转化为最小堆，线性时间
    heapq.heapify(arr)
    print("最小堆数组：{0}".format(arr))

    # 插入元素
    heapq.heappush(arr, 5)
    print("插入新元素后：{0}".format(arr))

    # 弹出最小元素
    item0 = heapq.heappop(arr)
    print("弹出的元素后：{0}".format(arr))

    # 返回最小元素
    item1 = arr[0]
    print("获取最小元素的值：{0}".format(item1))

    # 弹出最小元素，并插入一个新的元素，相当于先 heappop, 再 heappush
    item2 = heapq.heapreplace(arr, -2)
    print("弹出的元素为：{0}".format(item2))
    print("现在的堆结构为：{0}".format(arr))


class MyPriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        """
        队列由 (priority, index, item) 形式组成
        priority 增加 "-" 号是因为 heappush 默认是最小堆
        index 是为了当两个对象的优先级一致时，按照插入顺序排列
        """
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        """
        弹出优先级最高的对象
        """
        return heapq.heappop(self._queue)[-1]

    def qsize(self):
        return len(self._queue)

    def empty(self):
        return True if not self._queue else False


class Car(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return "{0} -- {1}".format(self.name, self.value)


if __name__ == "__main__":
    # arr = [1, 6, 9, 2, 4, 5, 3]
    # smallest_queue_test(arr)

    car1 = Car("BMW", 45)
    car2 = Car("Maybach", 145)
    car3 = Car("Bugatti", 85)
    car4 = Car("Cadillac", 78)
    car5 = Car("Maserati", 85)
    pq = MyPriorityQueue()
    pq.push(car1, car1.value)
    pq.push(car2, car2.value)
    pq.push(car3, car3.value)
    pq.push(car4, car4.value)
    pq.push(car5, car5.value)
    print("队列大小：{0}".format(pq.qsize()))
    # 弹出元素
    while not pq.empty():
        print(pq.pop())
