"""
Floyd-Warshall(可以计算负权值, 但不能计算负权回路)算法计算任意两点间最短路径, 时间复杂度为O(n^3), 空间复杂度为O(n^2)
"""

import numpy as np


def floyd(d):
    n, _ = d.shape
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i, k] + d[k, j] < d[i, j]:
                    d[i, j] = d[i, k] + d[k, j]
    return d


if __name__ == "__main__":
    d = np.ones((4, 4)) * np.inf
    for i in range(4):
        d[i, i] = 0

    d[0, 1] = 2
    d[0, 2] = 6
    d[0, 3] = 4

    d[1, 2] = 3

    d[2, 0] = 7
    d[2, 3] = 1

    d[3, 0] = 5
    d[3, 2] = 12

    d = floyd(d)
    print(d)