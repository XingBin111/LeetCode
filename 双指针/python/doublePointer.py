class ListNode:
    def __init__(self, data=0):
        self.data = data
        self.next = None


class DoublePointer:

    @staticmethod
    def has_cycle(head: ListNode):
        """
        检测列表中是否包含环
        """
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:        # 如果有环, 那么fast会在环里面领先slow一圈
                return True
        return False

    @staticmethod
    def detectCycle(head: ListNode):
        """
        返回环的起始节点
        """
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        if fast is None or fast.next is None:
            return ListNode(-1)
        slow = head
        while fast != slow:         # why? 可以看作者贴的图片, 讲解很清晰
            fast = fast.next
            slow = slow.next
        return slow

    @staticmethod
    def findMiddle(head: ListNode):
        """
        返回列表中点
        """
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow


    @staticmethod
    def reciprocal(head: ListNode, k: int):
        """
        返回列表中倒数第k个元素
        """
        fast = head
        slow = head
        while k > 0:
            fast = fast.next
            k -= 1

        while fast:
            fast = fast.next
            slow = slow.next
        return slow


def use_cycle():
    head = ListNode(0)
    node = head
    for i in range(1, 4):
        node.next = ListNode(i)
        node = node.next

    print(DoublePointer.has_cycle(head))
    circle_node = node

    for i in range(4, 9):
        node.next = ListNode(i)
        node = node.next
    node.next = circle_node

    print(circle_node.data)
    print(DoublePointer.detectCycle(head).data)


def use_middle_and_reciprocal():
    head = ListNode(0)
    node = head
    for i in range(1, 9):
        node.next = ListNode(i)
        node = node.next

    print(DoublePointer.findMiddle(head).data)
    print(DoublePointer.reciprocal(head, 3).data)


if __name__ == "__main__":
    # use_cycle()
    use_middle_and_reciprocal()
