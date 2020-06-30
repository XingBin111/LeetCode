class HashMap:
    def __init__(self, volume=5):
        self.volume = volume

        # None表示空桶, -1表示lazy remove
        self.entities = [None] * self.volume
        self.size = 0
        self.load_factor = 0.5

    def insert(self, key, val):
        hash_val = hash(key)
        idx = hash_val % self.volume
        key_in_map = False
        # 找到空桶或lazy remove桶时就结束循环
        while self.entities[idx] is not None:

            # 找到lazy remove
            if self.entities[idx][0] == -1:
                break
            # 找到相同的key
            elif self.entities[idx][1] == key:
                key_in_map = True
                break
            else:
                idx += 1
                idx = idx % self.volume

        self.entities[idx] = [hash_val, key, val]
        if not key_in_map:
            self.size += 1

            if self.size / self.volume > self.load_factor:
                self.expand()

    def expand(self):
        new_volume = self.volume * 2
        new_entities = [None] * new_volume
        for i, e in enumerate(self.entities):
            if e is not None and e[0] != -1:
                new_entities[i] = e

        self.entities = [None] * new_volume
        self.volume = new_volume
        self.size = 0
        for i, e in enumerate(new_entities):
            if e is not None:
                self.insert(e[1], e[2])

    def get(self, key):
        hash_val = hash(key)
        idx = hash_val % self.volume

        i = 0
        # 沿着非空桶的链进行查找
        while self.entities[idx] is not None:
            if self.entities[idx][1] == key and self.entities[idx][0] != -1:
                return self.entities[idx][2]
            else:
                i += 1
                idx += 1
                idx = idx % self.volume
            if i >= self.volume:
                break
        print("{} not in map".format(key))
        return None

    def delete(self, key):
        hash_val = hash(key)
        idx = hash_val % self.volume

        i = 0
        # 沿着非空桶的链进行查找
        while self.entities is not None:
            if self.entities[idx][1] == key:
                self.entities[idx][0] = -1
                self.size -= 1
                return
            else:
                i += 1
                idx += 1
                idx = idx % self.volume
            if i >= self.volume:
                break
        print("{} not in map".format(key))
        return


class HashMapI:
    def __init__(self, volume=5):
        self.volume = volume

        # None表示空桶, -1表示lazy remove
        self.entities = [None] * self.volume
        self.size = 0
        self.load_factor = 0.5

    # 沿key对应的查找链, 跳过所有冲突和lazy_remove的桶, 直到找到key相同的桶或空桶, 供查找和删除使用
    def probe4Hit(self, key):
        hash_val = hash(key)
        idx = hash_val % self.volume
        while self.entities[idx] is not None and key != self.entities[idx][1]:
            idx = (idx + 1) % self.volume
        return idx

    # 沿key对应的查找链, 找到首个可用的空桶或lazy_remove的桶, 供插入使用
    def probe4Free(self, key):
        hash_val = hash(key)
        idx = hash_val % self.volume
        while self.entities[idx] is not None:
            if self.entities[idx][0] == -1 or key == self.entities[idx][1]:
                break
            else:
                idx = (idx + 1) % self.volume
        return idx

    def insert(self, key, val):
        hash_val = hash(key)
        idx = self.probe4Free(key)

        self.entities[idx] = [hash_val, key, val]
        self.size += 1

        if self.size / self.volume > self.load_factor:
            self.expand()

    def expand(self):
        new_volume = self.volume * 2
        new_entities = [None] * new_volume
        for i, e in enumerate(self.entities):
            if e is not None and e[0] != -1:
                new_entities[i] = e

        self.entities = [None] * new_volume
        self.volume = new_volume
        self.size = 0
        for i, e in enumerate(new_entities):
            if e is not None:
                self.insert(e[1], e[2])

    def get(self, key):
        idx = self.probe4Hit(key)
        if self.entities[idx] is None or self.entities[idx][1] == -1:
            return False
        else:
            return self.entities[idx][2]

    def delete(self, key):
        idx = self.probe4Hit(key)
        if self.entities[idx] is None or self.entities[idx][1] == -1:
            return False
        self.entities[idx][0] = -1
        self.size -= 1
        return True


if __name__ == "__main__":
    d = HashMapI()
    d.insert('a', 1)

    d.insert('b', 2)

    d.insert('c', 3)

    print(d.get('a'))

    d.insert('a', 2)

    print(d.get('a'))

    d.delete("a")

    d.get("a")

    d.insert("d", 4)
    d.insert("d", 5)
