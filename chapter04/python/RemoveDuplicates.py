"""
删除数组中的元素时, 要尽量避免删除中间或头部元素, 尽量把要删除的元素交换到最后.
"""


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


# 使用快慢指针, 保证区间[0, slow]为不重复且有序的数组
def remove_arr_duplicates(nums):
    n = len(nums)
    slow = 0
    fast = 1

    while fast < n:
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] = nums[fast]

        fast += 1
    while fast > slow + 1:
        nums.pop()
        fast -= 1
    return slow


def remove_list_duplicates(head):
    slow = head
    fast = head.next
    l = 1
    while fast is not None:
        if slow.val != fast.val:
            slow = slow.next
            slow.val = fast.val
            l += 1

        fast = fast.next

    slow.next = None
    return l


if __name__ == "__main__":
    nums = [0, 0, 1, 1, 2, 2, 3, 3, 4]

    head = ListNode(nums[0])
    tmp = head
    for i in range(1, len(nums)):
        tmp.next = ListNode(nums[i])
        tmp = tmp.next

    print(remove_arr_duplicates(nums))
    print(nums)

    print(remove_list_duplicates(head))
    while head is not None:
        print(head.val)
        head = head.next