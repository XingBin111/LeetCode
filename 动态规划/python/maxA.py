"""
键盘上有以下4个键(组合键也只算成一个键):
1. A: 在屏幕上打印出"A"
2. ctrl-A: 选中整个屏幕
3. ctrl-C: 复制选中内容到缓冲区
4. ctrl-V: 将缓冲区内容显示到屏幕

你只能按N次键,  请问屏幕上最多可输出几个"A"
"""

import numpy as np


def maxA(N):
    """
    状态定义(定义状态很关键, 决定了dp的难度):
    1. 剪切板中A的数量为copy
    2. 当前屏幕上A的数量 a_num
    3. 当前剩余操作数

    但在LeetCode中提交会超时, 状态总数为N*a_num*copy, 而a_num和copy与N有关, 所以复杂度为O(N^3), 很不理想
    """
    d = {}
    def dp(n, a_num, copy):
        if n <= 0:
            return a_num
        if (n, a_num, copy) in d:
            return d[(n, a_num, copy)]
        res = max(
            dp(n-1, a_num+1, copy),         # 直接按A键
            dp(n-1, a_num+copy, copy),      # 按ctrl-V键
            dp(n-2, a_num, a_num),          # 按ctrl-A和ctrl-C键
        )
        d[(n, a_num, copy)] = res
        return res
    return dp(N, 0, 0)


def maxA_fast(N):
    """
    次数最多的A一定出现在类似于：
    A, ..., A, ctrl-A, ctrl-C, ctrl-V, ..., ctrl-V, A, ..., A, ctrl-A, ctrl-C, ctrl-V, ..., ctrl-V, ....
    即最后一个键一定是A或ctrl-V。
    dp中第i个元素表示按键i次，屏幕上出现最多的A的个数，另外假设在第j次是最后一次按ctrl-C，所以从第j次开始的按键为：ctrl-V, ..., ctrl-V

    按键：..., A, ctrl-A, ctrl-C, ctrl-V
    索引：    j-2  j-1      j
    """
    dp = [0] * (N+1)
    for i in range(1, N+1):
        dp[i] = dp[i-1] + 1
        for j in range(2, i):
            dp[i] = max(dp[i], dp[j-2]*(i-j+1))
    return dp[N]


if __name__ == "__main__":
    N = 11
    print(maxA(N))
    print(maxA_fast(N))
