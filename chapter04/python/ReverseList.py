class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


# 翻转整个链表
def reverse_list(head):
    if head.next is None:
        return head

    new_head = reverse_list(head.next)
    head.next.next = head
    head.next = None
    return new_head


# 翻转前k个节点
def reverse_list_k(head, k):
    if head.next is None or k == 1:
        return head
    new_head = reverse_list_k(head.next, k-1)
    tmp_node = head.next.next
    head.next.next = head
    head.next = tmp_node
    return new_head


# 翻转区间[a, b)中的节点
def reverse_list_between(a, b):
    pre = None
    cur = a

    while cur != b:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    return pre


def reverse_list_group(head, k):
    if head is None:
        return None

    a = head
    b = head
    for i in range(k):
        if b is None:
            return head
        b = b.next

    new_head = reverse_list_between(a, b)
    a.next = reverse_list_group(b, k)
    return new_head


def show_list(head):
    tmp = head

    while tmp is not None:
        print(tmp.val)
        tmp = tmp.next


if __name__ == "__main__":
    head = ListNode()

    tmp = head

    for i in range(1, 6):
        tmp.next = ListNode(i)
        tmp = tmp.next

    # show_list(head)
    new_head = reverse_list_group(head, 4)
    show_list(new_head)
