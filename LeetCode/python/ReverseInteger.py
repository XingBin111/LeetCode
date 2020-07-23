"""
难点在于c++中要考虑int32的溢出
"""


def reverse_integer(n):
    res = 0
    while n > 0:
        res = res * 10 + n % 10
        n = n // 10
    return res


if __name__ == "__main__":
    n = 123
    print(reverse_integer(n))