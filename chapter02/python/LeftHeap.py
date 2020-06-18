"""
二叉堆A元素个数为n, 二叉堆B元素个数为m, 将A与B合并成新的二叉堆:
方法1: 删除B的元素, 并插入A, 效率为O(mlog(m+n))
方法2: Floyd构造堆算法, 效率为O(m+n), 没有利用A和B的堆序性

合并效率太低, 需要改进
左式堆: 二叉堆的变种, 在保持堆序性的条件下, 附加新的条件, 使得堆合并过程中只调整很少的节点(O(logn))

左式堆拓扑结构上不一定是完全二叉树, 但堆的本质就是堆序性, 而不是完全二叉树, 不矛盾, 所以用树性结构取代向量
"""


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.lc = None
        self.parent = None
        self.rc = None
        self.npl = 1


def swap(a, b):
    tmp = a
    a = b
    b = tmp


# 只实现了接口, 没有实现构造函数
class LeftHeap:
    def get_max(self, a, b):
        pass

    def del_max(self, a):
        left_heap = a.lc
        right_heap = a.rc
        e = a.val
        new_root = self.merge(left_heap, right_heap)
        if new_root is not None:
            new_root.parent = None
        return e

    def insert(self, a, e):
        node = TreeNode(e)
        new_root = self.merge(a, node)
        new_root.parent = None

    def merge(self, a, b):
        if a is None:
            return b
        if b is None:
            return a
        if a.val < b.val:
            swap(a, b)

        a.rc = self.merge(a.rc, b)
        a.rc.parent = a
        if a.lc is None or a.lc.npl < a.rc.npl:
            swap(a.lc, a.rc)
        a.npl = a.rc.npl+1 if a.rc is not None else 1
        return a

