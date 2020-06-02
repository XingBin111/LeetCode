"""
今天你能够参加好几个活动, 每个活动开始和结束的时间用[start, end]表示, 你不能同时参加2个活动,
问题: 你一天最多能参加几个活动?
显然是求出这些时间区间的最大不相交子集

解决思路:
    1. 从区间集合intvs选择一个区间x, x是所有区间中结束最早的(end最小)
    2. 把所有与x相交的区间从intvs中删除.
    3. 重复1和2, 直到区间集合intvs为空
时间复杂度为O(N)
"""


def interval_schedule_while(intvs):
    intvs = sorted(intvs, key=lambda e: e[1])
    start = 0
    n = len(intvs)
    valid_interval_num = 0
    while start < n:
        jump = 0
        for i in range(start, n):
            if intvs[i][0] < intvs[start][1]:
                jump += 1
        start += jump
        valid_interval_num += 1
    return valid_interval_num


def interval_schedule_for(intvs):
    intvs = sorted(intvs, key=lambda e: e[1])
    n = len(intvs)
    valid_interval_num = 1
    x_end = intvs[0][1]
    for i in range(n):
        if intvs[i][0] >= x_end:
            valid_interval_num += 1
            x_end = intvs[i][1]
    return valid_interval_num


def erase_overlap_intervals(intvs):
    """
    给定一个区间的集合, 找到需要移除区间的最小数量, 使剩余区间互不重叠
    """
    return len(intvs) - interval_schedule_for(intvs)


if __name__ == "__main__":
    intvs = [[1, 3], [3, 6]]
    print(interval_schedule_while(intvs))
