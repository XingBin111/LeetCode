import math


def cal_eating_time(nums, speed):
    t = 0
    for e in nums:
        t += math.ceil(e / speed)
    return t


def min_eating_speed_violence(nums, H):
    speed = 1
    while cal_eating_time(nums, speed) > H:
        speed += 1
    return speed


# 时间复杂度O(N*logN)
def min_eating_speed_bin_search(nums, H):
    max_speed = max(nums)
    lo = 1
    hi = max_speed
    while lo <= hi:
        mid = (lo + hi) // 2
        t = cal_eating_time(nums, mid)
        if t > H:
            lo = mid + 1        # 速度增加
        else:
            hi = mid - 1        # 速度降低

    return lo


if __name__ == "__main__":
    # nums = [30, 11, 23, 4, 20]
    nums = [3, 6, 7, 11]
    H = 8
    print(min_eating_speed_bin_search(nums, H))
