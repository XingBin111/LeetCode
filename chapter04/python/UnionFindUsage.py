from chapter04.python.UnionFind import UnionFind


def solve(board):
    if len(board) == 0:
        return

    m = len(board)
    n = len(board[0])

    uf = UnionFind(m * n + 1)
    dummy = m * n

    for i in range(m):
        if board[i][0] == "o":
            uf.union(i * n, dummy)
        if board[i][n-1] == "o":
            uf.union(i * n + n - 1, dummy)

    for j in range(n):
        if board[0][j] == "o":
            uf.union(j, dummy)
        if board[m-1][j] == "o":
            uf.union(n * (m - 1) + j, dummy)

    d = [
        [1, 0],
        [0, 1],
        [0, -1],
        [-1, 0],
    ]
    for i in range(1, m-1):
        for j in range(1, n-1):
            if board[i][j] == "o":
                for k in range(4):
                    x = i + d[k][0]
                    y = j + d[k][1]
                    if board[x][y] == "o":
                        uf.union(x * n + y, i * n + j)

    for i in range(1, m-1):
        for j in range(1, n-1):
            if not uf.connected(dummy, i * n + j):
                board[i][j] = "x"


def solve_equation(equations):
    uf = UnionFind(26)
    a_ord = ord('a')
    for eq in equations:
        if eq[1] == "=":
            p = ord(eq[0])-a_ord
            q = ord(eq[-1])-a_ord
            uf.union(p, q)

    for eq in equations:
        if eq[1] == "!":
            p = ord(eq[0]) - a_ord
            q = ord(eq[-1]) - a_ord
            if uf.connected(p, q):
                return False
    return True


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

    equations = [
        ["a==b", "b!=c", "c==a"],
        ["c==c", "b==d", "x!=z"]
    ]

    for e in equations:
        print(solve_equation(e))