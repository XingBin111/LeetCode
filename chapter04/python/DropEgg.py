
# 时间复杂度O(K*N^2), 空间复杂度O(KN)


def drop_egg(n, k):
    dp_table = {}
    def helper(n, k):

        if k == 1:
            return n

        if n == 0:
            return 0

        if (k, n) in dp_table:
            return dp_table[(k, n)]
        res = float("inf")
        for i in range(1, n+1):
            res = min(res,
                      max(drop_egg(n - i, k), drop_egg(i - 1, k - 1)) + 1
                      )
        dp_table[(k, n)] = res
        return res
    return helper(n, k)


# 时间复杂度O(K*N*logN), 空间复杂度O(KN)

def drop_egg_bin_search(n, k):
    dp_table = {}

    def helper(n, k):

        if k == 1:
            return n

        if n == 0:
            return 0

        if (k, n) in dp_table:
            return dp_table[(k, n)]
        res = float("inf")
        lo = 1
        hi = n
        while lo <= hi:
            mid = (lo + hi) // 2
            not_broken = drop_egg(n - mid, k)
            broken = drop_egg(mid - 1, k - 1)
            if not_broken > broken:
                lo = mid + 1
                res = min(not_broken + 1, res)
            else:
                hi = mid - 1
                res = min(broken + 1, res)

        dp_table[(k, n)] = res
        return res

    return helper(n, k)


# 时间复杂度O(KN)

def drop_egg_super(n, k):
    import numpy as np
    dp_table = np.zeros((k+1, n+1), np.int32)

    m = 0
    while dp_table[k, m] < n:
        m += 1
        for i in range(1, k+1):
            dp_table[i, m] = dp_table[i, m-1] + dp_table[i-1, m-1] + 1
    return m


if __name__ == "__main__":
    n = 100
    k = 2
    print(drop_egg_super(n, k))
