"""
对n*n的矩阵做顺时针90度旋转

(i, j) ---> (j, n-i)
|               |
|               |
(n-j, i) <--- (n-i, n-j)

"""


def rotate(nums):
    n = len(nums) - 1
    for i in range(int((n+1)/2)):
        for j in range(i, n-i):
            tmp = nums[n-j][i]
            nums[n-j][i] = nums[n-i][n-j]
            nums[n - i][n - j] = nums[j][n-i]
            nums[j][n - i] = nums[i][j]
            nums[i][j] = tmp


if __name__ == "__main__":
    nums = [
          [5, 1, 9, 11],
          [2, 4, 8, 10],
          [13, 3, 6, 7],
          [15, 14, 12, 16]
        ]

    rotate_nums = [
          [15, 13, 2, 5],
          [14, 3, 4, 1],
          [12, 6, 8, 9],
          [16, 7, 10, 11]
        ]
    rotate(nums)
    for i in range(len(nums)):
        print(nums[i])
