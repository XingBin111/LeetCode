def super_egg_drop(K, N):
    """
    :param K: 鸡蛋数
    :param N: 楼层数
    :return: 找到鸡蛋恰好摔不碎的那层楼, 在最坏情况, 所需要的最少尝试次数
    """
    def dp(K, N):
        if K == 1:
            return N
        if N == 0:
            return 0

        res = float('inf')
        for i in range(1, N+1):
            res = min(
                res,
                max(dp(K-1, i-1), dp(K, N-i-1)) + 1,
                      )
        return res
    return dp(K, N)


def super_egg_drop_table(K, N):
    """
    时间复杂度: O(K*N^2), 空间复杂度O(KN)
    """
    d = {}
    def dp(K, N):
        if K == 1:
            return N
        if N == 0:
            return 0
        if (K, N) in d:
            return d[(K, N)]
        res = float('inf')
        for i in range(1, N+1):
            res = min(
                res,
                max(dp(K-1, i-1), dp(K, N-i-1)) + 1,    # 最坏情况下, 所以取max
                      )
        d[(K, N)] = res
        return res
    return dp(K, N)


def super_egg_drop_table_bin_search(K, N):
    """
    使用二分查找来改进算法, 时间复杂度: O(K*N*logN), 空间复杂度O(KN)
    """
    d = {}
    def dp(K, N):
        if K == 1:
            return N
        if N == 0:
            return 0
        if (K, N) in d:
            return d[(K, N)]
        res = float('inf')
        lo = 1
        hi = N
        while lo <= hi:
            mid = (lo + hi) // 2
            broken = dp(K-1, mid-1)
            not_broken = dp(K, N-mid-1)
            if broken > not_broken:
                hi = mid - 1
                res = min(res, broken + 1)
            else:
                lo = mid + 1
                res = min(res, not_broken + 1)

        d[(K, N)] = res
        return res
    return dp(K, N)


# def super_egg_drop_itertion(K, N):
#     """
#     迭代版本, 时间复杂度: O(K*N), 空间复杂度O(KN)
#     """
#     import numpy as np
#     dp_table = np.zeros((K+1, N+1))
#     m = 0
#     while dp_table[K, m] < N:
#         m += 1
#         for k in range(1, K+1):
#             dp_table[k, m] = dp_table[k, m-1] + dp_table[k-1, m-1] + 1
#     return m


if __name__ == "__main__":
    print(super_egg_drop_table_bin_search(2, 10))
