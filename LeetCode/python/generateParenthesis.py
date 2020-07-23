"""
给定n, 求能生成多少有效括号

例如n = 4
res = [
    ((()))
    (()())
    (())()
    ()(())
    ()()()
]
"""


def backtrack(res, s, n, left, right):
    if len(s) == 2 * n:
        res.append(s)

    if left < n:
        backtrack(res, s+"(", n, left+1, right)

    if right < n and right < left:
        backtrack(res, s+")", n, left, right+1)


# left表示左括号的数量, right表示右括号的数量
def generate_parenthesis(n):
    res = []
    s = ""
    backtrack(res, s, n, 0, 0)
    return res


if __name__ == "__main__":
    n = 3
    res = generate_parenthesis(n)
    print(res)
