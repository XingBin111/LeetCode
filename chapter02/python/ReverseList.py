class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def reverse_list_iteration(head):
    if head is None or head.next is None:
        return head

    pre = head
    cur = head.next
    nxt = head.next.next
    pre.next = None
    while nxt is not None:
        cur.next = pre

        pre = cur
        cur = nxt
        nxt = nxt.next
    cur.next = pre
    return cur


def reverse_list_iterationN(head, N):
    """
    翻转前N个节点
    """
    tmp = head
    for i in range(N - 1):
        tmp = tmp.next
    nxt = tmp.next
    tmp.next = None

    new_head = reverse_list_iteration(head)
    head.next = nxt
    return new_head


def reverse_list_recursive(head):
    """
    翻转指定区间的单链表, 注意这里链表索引从1开始, 666
    """
    if head.next is None:
        return head

    last = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return last


def reverse_list_recursiveN(head, N, successor=None):
    """
    翻转前N个节点
    """
    if N == 1:
        successor = head.next
        return head, successor
    else:
        successor = None
    last, successor = reverse_list_recursiveN(head.next, N - 1, successor)
    head.next.next = head
    head.next = successor
    return last, successor


def reverse_list_recursive_betweenMN(head, M, N):
    """
    翻转区间[M, N]中的节点, 666
    """
    if M == 1:
        return reverse_list_recursiveN(head, N)[0]

    head.next = reverse_list_recursive_betweenMN(head.next, M - 1, N - 1)
    return head


def show_list(head):
    tmp = head
    while tmp is not None:
        print(tmp.val)
        tmp = tmp.next


if __name__ == "__main__":
    head = ListNode(1)
    tmp = head
    for i in range(2, 7):
        tmp.next = ListNode(i)
        tmp = tmp.next
    print("before sort: ")
    show_list(head)

    print("after sort: ")
    head = reverse_list_recursive_betweenMN(head, 2, 4)
    show_list(head)
