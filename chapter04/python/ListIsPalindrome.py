"""
判断单链表是否为回文串
"""


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


# 倒序遍历单链表
def back_traverse(head):
    if head is None:
        return

    back_traverse(head.next)
    print(head.val)


# 时间O(N), 空间O(N)
def list_is_palindrome_stack(head):
    stack = []
    tmp = head
    while tmp is not None:
        stack.append(tmp.val)
        tmp = tmp.next

    tmp = head
    while tmp is not None:
        if tmp.val == stack.pop():
            tmp = tmp.next
        else:
            return False
    return True


def reverse_list(head):
    pre = None
    cur = head

    while cur is not None:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    return pre


# 时间O(N), 空间O(1)
def list_is_palindrome_double_pointer(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    # 找到中点
    if fast is not None:
        slow = slow.next

    # 翻转单链表
    new_head = reverse_list(slow)

    while new_head is not None:
        if head.val == new_head.val:
            head = head.next
            new_head = new_head.next
        else:
            return False
    return True


if __name__ == "__main__":
    head = ListNode(1)

    tmp = head

    tmp.next = ListNode(1)
    tmp = tmp.next

    tmp.next = ListNode(2)
    tmp = tmp.next

    # tmp.next = ListNode(2)
    # tmp = tmp.next

    tmp.next = ListNode(1)
    tmp = tmp.next

    tmp.next = ListNode(1)
    tmp = tmp.next

    print(list_is_palindrome_stack(head))
    print(list_is_palindrome_double_pointer(head))

