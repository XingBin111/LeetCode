def is_valid_traverse(tmp_res, t):
    for e in t:
        if e not in tmp_res:
            return False
    return True


class MinWindowTraverse:
    """
    寻找s中覆盖t所有字符的最小子串:
    例如, s="EBBANCF", t="ABC", 那么s中能够覆盖t中所有字符的最小子串为"BANC".
    使用[left, right]这个滑动窗口在s上移动, 如果[left, right]无法覆盖t, 那么right就右移(寻找解),
    如果[left, right]能够覆盖t, 那么left就右移(优化找到的解).

    时间复杂度为O(len(s)*len(t)), 因为在每个while循环中都要遍历t
    """

    @staticmethod
    def sliding_window(s, t):
        right = 0
        left = 0
        res = s

        flag = False            # 是否有解

        while right < len(s):
            tmp_res = s[left: right+1]
            if is_valid_traverse(tmp_res, t):       # 使用遍历的方法校验是否覆盖
                if len(tmp_res) < len(res):
                    res = tmp_res
                    flag = True
                left += 1
            else:
                right += 1

        return res if flag else ""


class MinWindowDict:
    """
    使用字典来校验是否覆盖, 时间复杂度为O(len(s) + len(t)
    虽然while嵌套while, 但双指针走过的路径最多为2*O(len(s))
    """

    @staticmethod
    def sliding_window(s, t):
        right = 0
        left = 0
        matches = 0
        needs = {}
        window = {}

        res = ""
        minLen = len(s) + 1

        for e in t:
            needs[e] = needs.get(e, 0) + 1

        while right < len(s):
            c1 = s[right]
            if c1 in t:
                window[c1] = window.get(c1, 0) + 1
                if window[c1] == needs[c1]:                 # 小心
                    matches += 1                            # 对于重复的c1只需要加一次即可

            while matches == len(needs):                    # 找到解之后, 慢指针不断右移来找到最短的字符串, 直到不匹配为止
                if minLen < 1 + right - left:
                    res = s[left: right+1]

                c2 = s[left]
                if c2 in t:
                    window[c2] -= 1
                if window[c2] < needs[c2]:                  # 小心
                    matches -= 1                            # 未覆盖
                left += 1
            right += 1  # 快指针不断右移, 直到找到解
        return res if minLen == (len(s)+1) else ""


if __name__ == "__main__":
    s = "EBBANCF"
    t = "ABC"

    print(MinWindowTraverse.sliding_window(s, t))

