"""
连通域分析: 查找连通域, 并染色, 处理对象通常是一张二值化的图像(代码使用0和255), 按行或按列扫描图像所有像素, 前景像素为1, 背景像素为0,
label从2开始计数, 像素通常有4邻域或8邻域.

two-pass法: 扫描2遍图像, 第一遍扫描时赋予每个像素位置一个label, 扫描过程中同一个连通域内的像素集合中可能被
赋予一个或多个不同的label, 因此需要将这些属于同一个连通域但具有不同值的label合并, 这个功能由第二遍扫描(第二遍为逆序扫描)完成, 即
为一个连通域赋予一个相同的label(通常是该连通域中最小的label)

seed filling(种子填充法): 选取一个前景像素点作为种子, 然后根据连通域两个基本条件(像素相同,位置相邻), 将与种子相邻的前景像素合并到同一个像素集合中, 最后得到该像素集合则为一个连通区域
"""

import cv2
import numpy as np

# 4邻域的连通域和 8邻域的连通域
# [row, col]
NEIGHBOR_HOODS_4 = True
OFFSETS_4 = [[0, -1], [-1, 0], [0, 0], [1, 0], [0, 1]]

NEIGHBOR_HOODS_8 = False
OFFSETS_8 = [[-1, -1], [0, -1], [1, -1],
             [-1,  0], [0,  0], [1,  0],
             [-1,  1], [0,  1], [1,  1]]


# 找到每个连通域的索引
def reorganize(binary_img):
    index_map = []
    points = []
    index = -1
    rows, cols = binary_img.shape
    for row in range(rows):
        for col in range(cols):
            val = binary_img[row, col]
            if val == 0:
                continue
            if val in index_map:
                index = index_map.index(val)
                num = index + 1
            else:
                index = len(index_map)
                num = index + 1
                index_map.append(val)
                points.append([])
            binary_img[row, col] = num
            points[index].append([row, col])
    return binary_img, points


def neighbor_value(binarg_img, offsets, reverse=False):
    rows, cols = binary_img.shape
    label_idx = 0
    rows_ = [0, rows, 1] if not reverse else [rows-1, -1, -1]
    cols_ = [0, cols, 1] if not reverse else [cols-1, -1, -1]
    for row in range(rows_[0], rows_[1], rows_[2]):
        for col in range(cols_[0], cols_[1], cols_[2]):
            label = 256
            if binary_img[row, col] == 0:
                continue

            for offset in offsets:
                neighbor_row = min(max(0, row+offset[0]), rows-1)
                neighbor_col = min(max(0, col+offset[1]), cols-1)
                neighbor_val = binarg_img[neighbor_row, neighbor_col]
                if neighbor_val == 0:
                    continue
                label = neighbor_val if neighbor_val < label else label

            if label == 255:
                label_idx += 1
                label = label_idx
            binarg_img[row, col] = label
    return binarg_img


def two_pass(binary_img, neighbor_hoods):
    if neighbor_hoods == NEIGHBOR_HOODS_4:
        offsets = OFFSETS_4
    else:
        offsets = OFFSETS_8
    binary_img = neighbor_value(binary_img, offsets, False)
    binary_img = neighbor_value(binary_img, offsets, True)
    return binary_img


def recursive_seed(binary_img: np.array, seed_row, seed_col, offsets, num, max_num=100):
    rows, cols = binary_img.shape
    binary_img[seed_row][seed_col] = num
    for offset in offsets:
        neighbor_row = min(max(0, seed_row + offset[0]), rows - 1)
        neighbor_col = min(max(0, seed_col + offset[1]), cols - 1)
        val = binary_img[neighbor_row, neighbor_col]
        if val < max_num:
            continue
        binary_img = recursive_seed(binary_img, neighbor_row, neighbor_col, offsets, num, max_num)
    return binary_img


# max_num 表示连通域最多存在的个数, num-1为连通域个数
def seed_filling(binary_img, neighbor_hoods, max_num=100):
    if neighbor_hoods == NEIGHBOR_HOODS_4:
        offsets = OFFSETS_4
    else:
        offsets = OFFSETS_8

    num = 1
    rows, cols = binary_img.shape
    for row in range(rows):
        for col in range(cols):
            val = binary_img[row][col]
            if val <= max_num:
                continue
            binary_img = recursive_seed(binary_img, row, col, offsets, num, max_num=100)
            num += 1
    return binary_img


if __name__ == "__main__":
    binary_img = np.zeros((4, 7), dtype=np.int16)
    index = [[0, 2], [0, 5],
            [1, 0], [1, 1], [1, 2], [1, 4], [1, 5], [1, 6],
            [2, 2], [2, 5],
            [3, 1], [3, 2], [3, 4], [3, 6]]
    for i in index:
        binary_img[i[0], i[1]] = np.int16(255)

    print("原始二值图像")
    print(binary_img)

    # print("Two_Pass")
    # binary_img = two_pass(binary_img, NEIGHBOR_HOODS_8)
    # binary_img, points = reorganize(binary_img)
    # print(binary_img, points)

    print("Seed_Filling")
    binary_img = seed_filling(binary_img, NEIGHBOR_HOODS_8)
    binary_img, points = reorganize(binary_img)
    print(binary_img, points)
