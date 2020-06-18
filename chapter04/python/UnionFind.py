"""
并查集算法, 主要解决图论中的动态连通性问题
"""


class UnionFind:
    def __init__(self, n):
        self.count = n
        self.parent = list(range(n))

    # 返回x的根节点
    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    # 将p, q连接
    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return

        self.parent[root_p] = root_q
        self.count -= 1

    # 判断p, q是否连通
    def connected(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        return root_p == root_q

    # 返回图中有多少个连通分量
    def count(self):
        return self.count


if __name__ == "__main__":
    uf = UnionFind(10)
    uf.union(0, 1)

