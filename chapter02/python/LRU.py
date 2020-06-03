class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class DoubleList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0

    # 在链表头部添加x
    def addFirst(self, x):
        tmp_node = self.head.next

        self.head.next = x
        x.pre = self.head
        x.next = tmp_node
        tmp_node.pre = x
        self.size += 1

    # 删除x(x一定是存在的)
    def remove(self, x):
        x.pre.next = x.next
        x.next.pre = x.pre

        x.pre = None
        x.next = None
        self.size -= 1

    # 删除链表中最后一个节点, 并返回该节点
    def remove_last(self):
        x = self.tail.pre
        self.remove(x)
        return x.key, x.val

    def show(self):
        x = self.head.next
        for i in range(self.size):
            print("key: {}, val: {}\n".format(x.key, x.val))
            x = x.next


def dl_usage():
    dl = DoubleList()

    x = Node(3, 4)
    dl.addFirst(x)
    print("add a Node:\n")
    dl.show()

    print("add another Node:\n")
    dl.addFirst(Node(1, 2))
    dl.show()

    dl.remove(x)
    print("remove (3, 4)\n")
    dl.show()

    dl.addFirst(Node(5, 6))
    print("add (5, 6)\n")
    dl.show()

    _, _ = dl.remove_last()
    print("remove last\n")
    dl.show()


class LRUCache:
    def __init__(self, cap):
        self.cap = cap
        self.hash_map = {}
        self.cache = DoubleList()

    def put(self, key, val):
        x = Node(key, val)
        if key in self.hash_map:
            self.cache.remove(self.hash_map.get(key))
            self.cache.addFirst(x)
            self.hash_map[key] = x
        else:
            if self.cap == self.cache.size:
                last = self.cache.tail.pre
                self.hash_map.pop(last.key)
                self.cache.remove_last()
            self.cache.addFirst(x)
            self.hash_map[key] = x

    def get(self, key):
        if key in self.hash_map:
            return -1
        x = self.hash_map[key]
        self.put(x.key, x.val)


def lru_usage():
    lru = LRUCache(3)
    lru.put(1, 2)
    lru.put(3, 4)
    lru.put(1, 3)

    print(lru.hash_map)
    lru.cache.show()
    print("-------------")

    lru.put(5, 6)
    lru.put(7, 8)
    print(lru.hash_map)
    lru.cache.show()


if __name__ == "__main__":
    lru_usage()
