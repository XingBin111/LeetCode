"""
问题: 给定一个长度未知的链表, 设计一个算法, 只能遍历一次, 均匀随机的返回链表中的一个节点
也就是每个节点被选中的概率为1/n

先说结论(很容易证明)，当你遇到第 i 个元素时，应该有 1/i 的概率选择该元素，1 - 1/i 的概率保持原有的选择。

同理，如果要随机选择 k 个数，只要在第 i 个元素处以 k/i 的概率选择该元素，以 1 - k/i 的概率保持原有选择即可
"""
import numpy as np


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def get_random(head):
    p = head
    i = 0
    res = 0
    while p is not None:
        # 生成[0, i]之间的随机数
        r = np.random.randint(0, i + 1)

        if r == 0:
            res = p.val
        p = p.next
        i += 1
    return res


def get_random_k(head, k=1):
    p = head
    i = k
    res = [0] * k
    for i in range(k):
        res[i] = p.val
        p = p.next

    while p is not None:
        # 生成[0, i)之间的随机数
        r = np.random.randint(0, i + 1)

        if r < k:
            res[r] = p.val
        p = p.next
        i += 1
    return res


if __name__ == "__main__":
    head = ListNode()

    tmp = head
    for i in range(1, 5):
        tmp.next = ListNode(i)
        tmp = tmp.next
    print(get_random_k(head, 2))

