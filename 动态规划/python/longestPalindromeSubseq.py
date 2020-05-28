"""
如果一个字符串是回文串，那么在它左右分别加上一个相同的字符，那么它一定还是一个回文串
如果在一个不是回文字符串的字符串两端添加任何字符，得到的一定不是回文串
如果在回文串左右分别加不同的字符，得到的一定不是回文串
"""
import numpy as np


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


if __name__ == "__main__":
    s = "bb"
    print(longestPalindromeSubseq2(s))
