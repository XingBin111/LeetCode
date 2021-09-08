"""
如果一个字符串是回文串，那么在它左右分别加上一个相同的字符，那么它一定还是一个回文串
如果在一个不是回文字符串的字符串两端添加任何字符，得到的一定不是回文串
如果在回文串左右分别加不同的字符，得到的一定不是回文串
"""
import numpy as np


# 复杂度O(N^2)
def longestPalindromeSubseq1(s):
    dp_table = np.zeros((len(s), len(s)), dtype=np.int32)
    for i in range(len(s)):
        dp_table[i, i] = 1
        if i != (len(s) - 1) and s[i] == s[i + 1]:
            dp_table[i, i + 1] = 2
    res = s[0]
    for i in range(len(s) - 1, -1, -1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j] and s[i: j + 1] == s[i: j + 1][::-1]:
                dp_table[i, j] = dp_table[i + 1, j - 1] + 2
                if dp_table[i, j] > len(res):
                    res = s[i: j + 1]
            else:
                dp_table[i, j] = max(dp_table[i + 1, j], dp_table[i, j - 1])
    return res


# 复杂度O(N^2)
def longestPalindromeSubseq2(s):
    n = len(s)
    if n == 0:
        return s
    res = s[0]

    def extend(i, j):
        while i >= 0 and j < n and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i + 1: j]
    for i in range(n):
        s1 = extend(i, i)
        s2 = extend(i, i + 1)
        if max(len(s1), len(s2)) > len(res):
            res = s1 if len(s1) > len(s2) else s2
    return res


# 时间复杂度O(N)
# 参考: https://zhuanlan.zhihu.com/p/70532099
def Manacher(s):
    t = "$#"
    for e in s:
        t += e + "#"

    center_idx = 0
    max_len = 0
    n = len(t)
    C, R = 0, 0
    p = [0] * n
    for i in range(1, n-1):
        i_mirror = 2 * C - i
        if R > i:
            p[i] = min(p[i_mirror], R - i)
        else:
            p[i] = 0

        while i+1+p[i] < n and t[i+1+p[i]] == t[i-1-p[i]]:
            p[i] += 1

        if p[i] + i > R:
            C = i
            R = p[i] + C

        if p[i] > max_len:
            max_len = p[i]
            center_idx = i

    start = (center_idx - max_len) // 2
    return s[start:(start+max_len)]


if __name__ == "__main__":
    s = "wabwsw"
    print(Manacher(s))
