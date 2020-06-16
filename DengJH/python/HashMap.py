class HashMap:
    def __init__(self, volume=5):
        self.volume = volume
        self.indices = [-1] * self.volume
        self.entities = []

    def insert(self, key, val):
        hash_val = hash(key)
        entity = [hash_val, key, val]
        indice = hash_val % self.volume

        if self.indices[indice] != -1:
            # 如果哈希值相等, 就更新val
            if self.entities[self.indices[indice]][0] == hash_val:
                self.entities[self.indices[indice]][2] = val
                return
            # 否则就处理冲突
            else:
                # 寻找新的插入位置
                print("conflict:", key)
                while self.indices[indice] != -1:
                    indice += 1
                    if indice >= self.volume:
                        indice %= self.volume

        self.indices[indice] = len(self.entities)
        self.entities.append(entity)

        if len(self.entities) / self.volume > 0.5:
            self.expand()
        return

    def expand(self):
        print("expand")
        self.volume = 2 * self.volume
        self.indices = [-1] * self.volume
        old_entities = self.entities.copy()
        self.entities = []

        for hash_val, key, val in old_entities:
            self.insert(key, val)

    def get(self, key):
        hash_val = hash(key)
        indice = hash_val % self.volume
        if self.indices[indice] == -1:
            return None
        else:
            while self.entities[self.indices[indice]][0] != hash_val:
                indice += 1
                if indice >= self.volume:
                    indice %= self.volume
            return self.entities[self.indices[indice]][2]


if __name__ == "__main__":
    d = HashMap()
    d.insert('a', 1)

    d.insert('b', 2)

    d.insert('c', 3)

    print(d.get('a'))

    d.insert('a', 2)

    print(d.get('a'))
