class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class ListQuickSort:
    def partition(self, start_node, end_node):
        pivot = start_node.val
        mid_node = start_node
        node = start_node.next
        while node != end_node:
            if node.val < pivot:
                mid_node = mid_node.next
                mid_node.val, node.val = node.val, mid_node.val
            node = node.next
        start_node.val, mid_node.val = mid_node.val, start_node.val
        return mid_node

    def quick_sort(self, start_node, end_node):
        if start_node == end_node or start_node.next == end_node:
            return

        mid_node = self.partition(start_node, end_node)
        self.quick_sort(start_node, mid_node)
        self.quick_sort(mid_node.next, end_node)


class VectorQuickSort:
    def partition(self, nums, lo, hi):
        pivot = nums[lo]
        mi = lo
        for k in range(lo + 1, hi + 1):
            if nums[k] < pivot:
                mi += 1
                nums[mi], nums[k] = nums[k], nums[mi]
        nums[lo], nums[mi] = nums[mi], nums[lo]
        return mi

    # [lo, hi]
    def quick_sort(self, nums, lo=0, hi=0):
        if hi - lo < 1:
            return

        mi = self.partition(nums, lo, hi)
        self.quick_sort(nums, lo, mi - 1)
        self.quick_sort(nums, mi + 1, hi)


if __name__ == "__main__":
    nums = [6, 3, 8, 2, 5, 9, 4, 5, 1, 7]
    vqs = VectorQuickSort()
    vqs.quick_sort(nums, 0, len(nums)-1)
    # select_sort(nums)
    print(nums)

    nums = [6, 3, 8, 2, 5, 9, 4, 5, 1, 7]
    head = ListNode(nums[0])
    tmp = head
    for i in range(1, len(nums)):
        tmp.next = ListNode(nums[i])
        tmp = tmp.next
    lqs = ListQuickSort()
    lqs.quick_sort(head, None)
    res = []
    while head is not None:
        res.append(head.val)
        head = head.next
    print(res)