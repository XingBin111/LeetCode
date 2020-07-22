"""
找到两个单链表相交的起始节点。

两个指针分别指向A，B，同时出发，到达末端时分别交换head，再遍历一次，直到到达交点
"""


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def show_list(head):
    tmp = head

    while tmp is not None:
        print(tmp.val)
        tmp = tmp.next


def getIntersectionNode(headA, headB):
    a = headA
    b = headB
    while a != b:
        if a is not None:
            a = a.next
        else:
            a = headB

        if b is not None:
            b = b.next
        else:
            b = headA
    return a


if __name__ == "__main__":
    intersectVal = [8, 4, 5]
    listA = [4, 1]
    listB = [5, 0, 1]

    headA = ListNode(listA[0])
    headB = ListNode(listB[0])

    tmpA = headA
    tmpB = headB

    tmpA.next = ListNode(listA[1])
    tmpA = tmpA.next

    tmpB.next = ListNode(listB[1])
    tmpB = tmpB.next

    tmpB.next = ListNode(listB[2])
    tmpB = tmpB.next

    headI = ListNode(intersectVal[0])
    tmpI = headI

    tmpI.next = ListNode(intersectVal[1])
    tmpI = tmpI.next

    tmpI.next = ListNode(intersectVal[2])
    tmpI = tmpI.next

    tmpA.next = headI
    tmpB.next = headI

    print("headA: ")
    show_list(headA)

    print("headB: ")
    show_list(headB)

    print("intersection: ")
    print(getIntersectionNode(headA, headB).val)