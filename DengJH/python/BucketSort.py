"""
给定范围为[0, M)内的n个互异整数(n<=M), 借助haspmap来排序，由于python的字典暂时不清楚如何遍历底层散列表，所以用list替代
时间效率为O(M+n),空间效率为O(M)
"""


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def bucket_sort(nums):
    M = max(nums) + 1
    assist_l = [0] * M
    res = [0] * len(nums)
    for e in nums:
        assist_l[e] = 1

    k = 0
    for i, e in enumerate(assist_l):
        if e != 0:
            res[k] = i
            k += 1
    return res


# 当nums中有重复的整数时，要使用链表来处理冲突元素, 最坏情况下时间效率为O（Mn）
def bucket_sort_conflict(nums):
    M = max(nums) + 1
    assist_l = [ListNode(0)] * M
    res = [0] * len(nums)
    for e in nums:
        node = ListNode(1)
        # 冲突
        if assist_l[e].val == 1:
            tmp_node = assist_l[e]
            while tmp_node.next is not None:
                tmp_node = tmp_node.next
            tmp_node.next = node
        else:
            assist_l[e] = ListNode(1)

    k = 0
    for i, e in enumerate(assist_l):
        if e.val == 1:
            while e is not None:
                res[k] = i
                k += 1
                e = e.next
    return res


if __name__ == "__main__":
    nums = [3, 9, 5, 8, 2]
    nums_conflict = [5, 2, 3, 2, 9, 5, 8, 2]
    print(bucket_sort(nums))
    print(bucket_sort_conflict(nums_conflict))
