class lengthOfLongestSubstring:
    """
    寻找无重复最长子串的长度:
    输入: pwwkew, 返回: 3, 无重复子串为"kew"
    """
    @staticmethod
    def lengthOfLongestSubstring(s):
        res = ""
        left = 0
        right = 0
        while right < len(s):
            c = s[right]
            tmp_res = s[left: right]
            if c in tmp_res:                # 会对tmp_res进行遍历, 时间效率较低
                left += 1
            else:
                right += 1
                if len(res) < len(s[left: right]):
                    res = s[left: right]

        return res

    @staticmethod
    def lengthOfLongestSubstringDict(s):
        res = []
        window = {}
        left = 0
        right = 0
        while right < len(s):
            c1 = s[right]
            window[c1] = window.get(c1, 0) + 1

            while window[c1] > 1:
                c2 = s[left]
                window[c2] -= 1
                left += 1

            right += 1
            if len(res) < len(s[left: right]):
                res = s[left: right]

        return res


if __name__ == '__main__':
    ss = ["abcabcbb", "bbbbb", "pwwkew"]
    for s in ss:
        print(lengthOfLongestSubstring.lengthOfLongestSubstringDict(s))