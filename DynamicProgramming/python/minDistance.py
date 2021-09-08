import numpy as np


def min_distance(s1, s2):
    def dp(i, j):
        if i == -1:
            return j + 1
        if j == -1:
            return i + 1
        if s1[i] == s2[j]:
            return dp(i - 1, j - 1)
        else:
            return min(
                dp(i - 1, j) + 1,       # 对s1进行删除
                dp(i, j - 1) + 1,       # 对s1进行插入
                dp(i - 1, j - 1) + 1      # 对s1进行替换
            )
    return dp(len(s1) - 1, len(s2) - 1)


def min_distance_table(s1, s2):
    table = {}

    def dp(i, j):
        if (i, j) in table:
            return table[(i, j)]
        if i == -1:
            return j + 1
        if j == -1:
            return i + 1
        if s1[i] == s2[j]:
            table[(i, j)] = dp(i - 1, j - 1)
        else:
            table[(i, j)] = min(dp(i - 1, j) + 1,
                   dp(i, j - 1) + 1, dp(i - 1, j - 1) + 1)
        return table[(i, j)]
    return dp(len(s1) - 1, len(s2) - 1)


def track_operation(dp_array):
    d = {0: "替换", 1: "删除", 2: "插入"}
    track = []
    i = dp_array.shape[0] - 1
    j = dp_array.shape[1] - 1
    while i > 0 and j > 0:
        tmp_l = [dp_array[i - 1, j - 1],
            dp_array[i - 1, j], dp_array[i, j - 1]]
        tmp_min = min(tmp_l)
        tmp_idx = tmp_l.index(tmp_min)

        if tmp_min < dp_array[i, j]:
            track.append(d[tmp_idx])

        if tmp_idx == 0:
            i -= 1
            j -= 1
        elif tmp_idx == 1:
            i -= 1
        elif tmp_idx == 2:
            j -= 1

    print(track)


def min_distance_iteration(s1, s2):
    s1 = "_" + s1
    s2 = "_" + s2
    dp_array = np.zeros((len(s1), len(s2)))
    for i in range(len(s1)):
        dp_array[i, 0] = i
    for i in range(len(s2)):
        dp_array[0, i] = i

    for i in range(1, len(s1)):
        for j in range(1, len(s2)):
            if s1[i] == s2[j]:
                dp_array[i, j] = dp_array[i-1, j-1]

            else:
                dp_array[i, j] = min(
                    dp_array[i - 1, j - 1] + 1,
                    dp_array[i, j - 1] + 1,
                    dp_array[i - 1, j] + 1,
                )
    track_operation(dp_array)
    return dp_array


if __name__ == "__main__":
    s1 = "rose"
    s2 = "horse"
    print(min_distance_iteration(s1, s2))
