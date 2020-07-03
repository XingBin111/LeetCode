class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def swap(i, j):
    i.val, j.val = j.val, i.val


# L = [lo, mi], G = [mi+1, k-1], U = [k, hi]
# 不稳定, 数值相同的元素, 在排序后可能不能保持原始次序
def partitionII(start, end):
    pivot = start.val
    mi = start
    cur = start.next
    while cur != end:
        if cur.val < pivot:
            swap(mi.next, cur)
            mi = mi.next
        cur = cur.next
    swap(start, mi)
    return mi

# 若每次划分平均(轴点的选取都接近中央), 时间效率为O(nlogn), 若每次划分都极不平均(轴点总是最大或最小元素), 时间效率为O(n^2)
# 但平均性能为O(nlogn), 搜索区间为[lo, hi)
def quick_sort(start, end):
    if start == end or start.next == end:
        return
    mi = partitionII(start, end)
    quick_sort(start, mi)
    quick_sort(mi.next, end)


if __name__ == "__main__":
    nums = [6, 3, 8, 2, 5, 9, 4, 5, 1, 7]
    head = ListNode(nums[0])
    tmp = head
    for i in range(1, len(nums)):
        tmp.next = ListNode(nums[i])
        tmp = tmp.next

    quick_sort(head, None)
    while head is not None:
        print(head.val)
        head = head.next

