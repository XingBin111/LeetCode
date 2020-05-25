class FindAnagrams:
    """
    找到字符串中所有字母异位词(字母相同, 但排列不同的字符串)
    输入: s="cbaebabacd", t="abc", 输出[0, 6]
    索引等于0的子串是"cba", 是t的异位词,
    索引等于6的子串是"bac", 是p的异位词.
    """

    @staticmethod
    def findAnagrams(s, t):
        res = []
        needs = {}
        window = {}
        for e in t:
            needs[e] = needs.get(e, 0) + 1
        left = 0
        right = 0
        matches = 0
        while right < len(s):
            c1 = s[right]
            if c1 in needs:
                window[c1] = window.get(c1, 0) + 1
                if window[c1] == needs[c1]:             # 小心
                    matches += 1

            while matches == len(needs):
                res.append(right - len(t) + 1)
                c2 = s[left]
                if c2 in needs:
                    window[c2] -= 1
                if window[c2] != needs[c2]:             # 小心
                    matches -= 1
                left += 1

            right += 1
        return res


if __name__ == "__main__":
    s = "cbaebabacd"
    t = "abc"
    print(FindAnagrams.findAnagrams(s, t))