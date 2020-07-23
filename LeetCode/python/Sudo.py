"""
IsValidSudo: 判断是否为有效的数独

SolveSudo: 解出数独
"""


class IsValidSudo:
    def is_valid_element(self, sudo_arr, row, col):
        e = sudo_arr[row][col]
        if e == ".":
            return True

        # 判断行
        for i in range(9):
            if col != i and sudo_arr[row][i] == e:
                return False

        # 判断列
        for i in range(9):
            if row != i and sudo_arr[i][col] == e:
                return False

        # 判断grid
        idx_row = row // 3
        idx_col = col // 3
        for i in range(3*idx_row, 3*(idx_row+1)):
            for j in range(3*idx_col, 3*(idx_col+1)):
                if i == row and j == col:
                    continue
                if sudo_arr[i][j] == e:
                    return False
        return True

    def is_valid_sudo(self, sudo_arr):
        for row in range(9):
            for col in range(9):

                if not self.is_valid_element(sudo_arr, row, col):
                    return False
        return True


class SolveSudo:
    def __init__(self):
        self.check_sudo = IsValidSudo()

    def backtrack(self, sudo_arr, row, col):
        if row == 9:
            return True
        if col == 9:
            return self.backtrack(sudo_arr, row+1, 0)
        if sudo_arr[row][col] != ".":
            return self.backtrack(sudo_arr, row, col+1)

        for i in range(9):
            sudo_arr[row][col] = str(i+1)
            if self.check_sudo.is_valid_element(sudo_arr, row, col):
                further_valid = self.backtrack(sudo_arr, row, col+1)
                if further_valid:
                    return True
        sudo_arr[row][col] = "."
        return False

    def solve_sudo(self, sudo_arr):
        self.backtrack(sudo_arr, 0, 0)


if __name__ == "__main__":
    sudo_arr = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    is_valid = IsValidSudo()
    print(is_valid.is_valid_sudo(sudo_arr))

    nums = [1, 2, 3]

    solve = SolveSudo()
    solve.solve_sudo(sudo_arr)
    for e in sudo_arr:
        print(e)
