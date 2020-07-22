import collections


offset = [[0, -1], [-1, 0], [0, 0], [1, 0], [0, 1]]


def solve(board):
    m = len(board)
    n = len(board[0])
    d = collections.deque()
    for i in range(m):
        for j in [0, n-1]:
            if board[i][j] == "o":
                d.append((i, j))

    for i in [0, m-1]:
        for j in range(n):
            if board[i][j] == "o":
                d.append((i, j))

    while len(d) > 0:
        (i, j) = d.popleft()

        if 0 <= i < m and 0 <= j < n and board[i][j] == "o":
            board[i][j] = "*"
            d.append((i - 1, j))
            d.append((i + 1, j))
            d.append((i, j - 1))
            d.append((i, j + 1))

    for i in range(m):
        for j in range(n):
            if board[i][j] == "*":
                board[i][j] = "o"
            elif board[i][j] == "o":
                board[i][j] = "x"


if __name__ == "__main__":
    board = [
        ["x", "x", "x", "x", "o"],
        ["x", "x", "x", "o", "x"],
        ["o", "o", "x", "o", "x"],
        ["x", "o", "x", "x", "x"],
    ]
    solve(board)

    for e in board:
        print(e)