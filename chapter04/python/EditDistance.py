

# 指针从后往前移动
def edit_distance(s1, s2):
    if len(s1) == 0:
        return len(s2)

    if len(s2) == 0:
        return len(s1)

    if s1[-1] == s2[-1]:
        return edit_distance(s1[:-1], s2[:-1])

    else:
        res = min(
            edit_distance(s1, s2[:-1]),        # 增
            edit_distance(s1[:-1], s2),                     # 删
            edit_distance(s1[:-1], s2[:-1])                # 替换
        )
        return res + 1


def edit_distance_iteration(s1, s2):
    import numpy as np
    n = len(s1)
    m = len(s2)
    dp_tale = np.zeros((n+1, m+1), dtype=np.int32)

    for i in range(n+1):
        dp_tale[i, 0] = i

    for i in range(m+1):
        dp_tale[0, i] = i
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i-1] == s2[j-1]:
                dp_tale[i, j] = dp_tale[i-1, j-1]
            else:
                res = min(
                    dp_tale[i - 1, j],
                    dp_tale[i, j - 1],
                    dp_tale[i - 1, j - 1],
                )
                dp_tale[i, j] = res + 1
    return dp_tale[n, m]


if __name__ == "__main__":
    s1 = "horse"
    s2 = "ros"
    print(edit_distance(s1, s2))
    print(edit_distance_iteration(s1, s2))