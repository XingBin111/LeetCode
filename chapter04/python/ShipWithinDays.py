def cal_ship_days(nums, ship_weight):
    cur_weight = 0
    d = 0
    for e in nums:
        cur_weight += e
        if cur_weight > ship_weight:
            cur_weight = e
            d += 1
    if cur_weight > 0:
        d += 1
    return d


def ship_within_days(nums, D):
    lo = 1
    hi = sum(nums)
    while lo <= hi:
        mid = (lo + hi) // 2
        d = cal_ship_days(nums, mid)
        if d > D:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo


if __name__ == "__main__":
    nums = list(range(1, 11))
    D = 5
    print(ship_within_days(nums, D))