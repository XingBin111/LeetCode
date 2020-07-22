"""
查找区间[0, n)中所有的素数
countPrimesI思路:
首先从2开始, 如果2是素数, 那么2*2, 3*2, 4*2....都不是素数
3是素数, 3*2, 3*3, 3*4...也都不是素数,

countPrimesII思路
countPrimesI存在计算冗余, 例如6被计算了2次, 可以让j从i**2开始遍历

复杂度:
n/2 + n/3 + n/5 + n/7 + ... = n × (1/2 + 1/3 + 1/5 + 1/7...)

最终结果是O(N*loglogN)
"""
import numpy as np


def isPrime(n):
    for i in range(2, int(np.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


# 暴力算法, 时间效率为O(n*sqrt(n))
def countPrimes(n):
    count = 0
    for i in range(2, n):
        if isPrime(i):
            count += 1
    return count


def countPrimesI(n):
    prim_arr = [True] * n
    for i in range(2, n):
        if prim_arr[i]:
            for j in range(2*i, n, i):
                prim_arr[j] = False
    count = 0
    for i in range(2, n):
        if prim_arr[i]:
            count += 1
    return count


def countPrimesII(n):
    prim_arr = [True] * n
    for i in range(2, int(np.sqrt(n))+1):
        if prim_arr[i]:
            for j in range(i**2, n, i):
                prim_arr[j] = False
    count = 0
    for i in range(2, n):
        if prim_arr[i]:
            count += 1
    return count


if __name__ == "__main__":
    n = 100
    print(countPrimes(n))
    print(countPrimesI(n))
    print(countPrimesII(n))
