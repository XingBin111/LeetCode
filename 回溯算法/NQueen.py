class Queen:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def is_conflict(self, q):
        if q.x == self.x or q.y == self.y or (q.x+q.y) == (self.x+self.y) or (q.x-q.y) == (self.x-self.y):
            return True
        else:
            return False

    def __repr__(self):
        return "x={}, y={}".format(self.x, self.y)


def is_valid(track, tmp_q):
    for q in track:
        if q.is_conflict(tmp_q):
            return True
    return False


# 在循环中递归
def backtrack(n, track):
    if len(track) == n:
        for q in track:
            if q.y == 0:
                print("Q" + "-" * (n-1))
            elif q.y == n-1:
                print("-" * (n - 1) + "Q")
            else:
                print("-"*(q.y-1) + "Q" + "-" * (n-1-q.y))
        return True
    for j in range(n):
        i = len(track)
        tmp_q = Queen(i, j)
        if is_valid(track, tmp_q):
            continue
        track.append(tmp_q)
        if backtrack(n, track):
            return True
        track.pop()


def solveNQueens(n):
    track = []
    backtrack(n, track)


solveNQueens(10)
