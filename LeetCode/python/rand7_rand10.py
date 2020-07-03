"""
使用rand7实现rand10. rand7可生成1到7范围内的均匀随机整数
"""

import random


def rand7():
    return random.randint(1, 7)


def rand10():
    """
    运行2次rand7(), 得到[0, 48]均匀随机整数, 选40个, 每4个映射到0~9, 然后加1, 就是rand10
    """
    r_0_48 = (rand7() - 1) * 7 + rand7() - 1
    while True:
        if r_0_48 <= 39:
            return r_0_48 // 4 + 1


if __name__ == "__main__":
    print(rand10())