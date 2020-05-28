"""
KMP算法用于字符串匹配, 首先约定pat表示模式串, 长度为M. txt表示文本串, 长度为N. KMP算法就是在txt中查找子串pat,
如果存在, 就返回这个子串在txt中的起始索引, 不存在返回-1
"""


def violence_kmp(pat, txt):
    """
    使用暴力算法求解. 时间效率为O(MN), 空间复杂度为O(1)
    使用该解法求pat = "aaab", txt = "aaacaaab", txt中字母"c"被反复比较, 但其实pat中根本不含"c", 所以没必要比较.
    """
    M = len(pat)
    N = len(txt)
    for i in range(N-M+1):
        if txt[i:i+M] == pat:
            return i
    return -1


def kmp(pat, txt):
    """
    kmp算法永不回退txt的指针(不会重复扫描txt), 而是借助dp数组中存储的信息把pat移动到正确的位置继续匹配, 以空间换时间,
    所以时间复杂度为O(N), 空间复杂度为O(M)
    """
    M = len(pat)
    N = len(txt)
    dp_table = {}
    txt_e = list(set(txt))
    for e in set(txt_e):
        dp_table[(0, e)] = 0
    dp_table[(0, pat[0])] = 1
    x = 0
    for j in range(1, M):
        for c in range(len(txt_e)):
            e = txt_e[c]
            dp_table[(j, e)] = dp_table[(x, e)]
        dp_table[(j, pat[j])] = j + 1
        x = dp_table[(x, pat[j])]   # 很关键, 还不是很懂

    j = 0
    for i in range(N):
        j = dp_table[(j, txt[i])]
        if j == M:
            return i - M + 1
    return -1


if __name__ == "__main__":
    pat = "ABABC"
    txt = "CABAABABAC"
    print(kmp(pat, txt))
