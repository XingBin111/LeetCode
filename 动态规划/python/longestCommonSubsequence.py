"""
最长公共子序列(lcs)
输入：s1 = “abcde”，s2 = “ace”
输出：3
解释：最长公共子序列位“ace”，长度为3
"""


def longestCommonSubsequence(s1, s2):
    def dp(i, j):
        if i == -1 or j == -1:
            return 0
        if s1[i] == s2[j]:              # 该字符一定属于lcs
            return dp(i-1, j-1) + 1
        else:                           # 至少有一个字符不在lcs中，取最长的那个
            return max(dp(i-1, j), dp(i, j-1))
    return dp(len(s1)-1, len(s2)-1)


def longestCommonSubsequenceMemo(s1, s2):
    d = {}
    def dp(i, j):
        if i == -1 or j == -1:
            return 0

        if (i, j) in d:
            return d[(i, j)]

        if s1[i] == s2[j]:              # 该字符一定属于lcs
            ans = dp(i-1, j-1) + 1
        else:                           # 至少有一个字符不在lcs中，取最长的那个
            ans = max(dp(i-1, j), dp(i, j-1))
        d[(i, j)] = ans
        return d[(i, j)]
    return dp(len(s1)-1, len(s2)-1)


def longestCommonSubsequenceIteration(s1, s2):
    import numpy as np
    m, n = len(s1), len(s2)
    dp = np.zeros((m+1, n+1), dtype=np.int32)
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i, j] = dp[i-1, j-1] + 1
            else:
                dp[i, j] = max(dp[i-1, j], dp[i, j-1])
    return dp


if __name__ == "__main__":
    s1 = "ab"
    s2 = "aaaaaa"
    print(longestCommonSubsequenceIteration(s1, s2))
