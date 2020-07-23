"""
合并k个有序列表
方法1: 如同归并排序那样两两合并, 时间为O(kn*logk), 空间为O(logk)
方法2: 使用优先级队列, 建立长度为k的优先级队列, 将每个列表的首元素放入优先级队列, 然后不断的取和存, 时间为O(kn*logk), 空间为O(k)
"""
from LeetCode.python.priorityQueue import MyPriorityQueue


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def build_list(nums):
    res = []
    for v in nums:
        head = ListNode(v[0])
        tmp = head
        for i in range(1, len(v)):
            tmp.next = ListNode(v[i])
            tmp = tmp.next
        res.append(head)
    return res


def show_list(head):
    while head is not None:
        print(head.val)
        head = head.next


# 时间: O(n), 空间O(1)
def merge_two_list(nodeA, nodeB):
    header = ListNode(0)
    tmp = header
    while nodeA is not None and nodeB is not None:
        if nodeA.val > nodeB.val:
            tmp.next = nodeB
            nodeB = nodeB.next
        else:
            tmp.next = nodeA
            nodeA = nodeA.next
        tmp = tmp.next

    if nodeA is not None:
        tmp.next = nodeA

    if nodeB is not None:
        tmp.next = nodeB
    return header.next


def merge(heads, lo, hi):
    if lo == hi:
        return heads[lo]

    mi = (lo + hi) // 2
    return merge_two_list(merge(heads, lo, mi), merge(heads, mi+1, hi))


# 第一轮合并k/2个链表, 每次时间为O(2n), 第二轮合并k/4个链表, 每次时间为O(4n), 第logk轮合并链表的时间为O(kn), 所以时间为O(kn*logk)
# 递归使用的空间为O(logk), 递归长度为O(logk), 每次递归使用的空间为O(1)
def merge_k_list(heads):
    return merge(heads, 0, len(heads)-1)


def merge_k_list_pq(heads):
    pq = MyPriorityQueue()
    for e in heads:
        pq.push(e, -e.val)

    header = ListNode(0)
    tmp = header
    while pq.qsize() > 0:
        node = pq.pop()
        if node.next is not None:
            pq.push(node.next, -node.next.val)
        tmp.next = node
        tmp = tmp.next
    return header.next


if __name__ == "__main__":
    nums = [
        [1, 4, 5],
        [1, 3, 4],
        [2, 6],
    ]

    heads = build_list(nums)

    # new_head = merge_two_list(heads[0], heads[2])
    # show_list(new_head)

    # new_head = merge_k_list(heads)
    # show_list(new_head)

    new_head = merge_k_list_pq(heads)
    show_list(new_head)