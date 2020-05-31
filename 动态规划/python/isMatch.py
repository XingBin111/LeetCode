"""
正则匹配，给定字符串s和p。实现支持" . "和" * "的正则匹配
" . "：匹配单个字符
" * "：匹配零个或多个前面的字符

------------------------------------------------

例1：输入 s = "aa", p = "a*", 返回True
例2：输入 s = "aab", p = "c*a*b", 返回True
例3：输入 s = "ab", p = ".*", 返回True
"""


def isMatch(text, pattern):
    if len(pattern) == 0:
        return len(text) == 0

    first_match = len(text) > 0 and pattern[0] in [".", text[0]]
    if len(pattern) >= 2 and pattern[1] == "*":
        # 匹配0次，即pattern右移2位
        # 匹配1次，即text右移1位，666
        return isMatch(text, pattern[2:]) or (first_match and isMatch(text[1:], pattern))
    else:
        return first_match and isMatch(text[1:], pattern[1:])


def isMatchMemo(text, pattern):
    d = {}
    def dp(i, j):
        if (i, j) in d:
            return d[(i, j)]
        if j == len(pattern):
            return len(text) == i

        first_match = len(text[i:]) > 0 and pattern[j] in [".", text[i]]
        if len(pattern[j:]) >= 2 and pattern[j+1] == "*":
            ans = dp(i, j+2) or (first_match and dp(i+1, j))

        else:
            ans = first_match and dp(i+1, j+1)
        d[(i, j)] = ans
        return ans
    return dp(0, 0)


if __name__ == "__main__":
    s = "aaabc"
    p = "a.*bcd"
    print(isMatchMemo(s, p))

