def intersection(a, b):
    if a[1] >= b[0]:
        return [b[0], a[1]]

    if b[1] >= a[0]:
        return [a[0], b[1]]
    return None


def interval_intersection(A, B):
    res = []

    i, j = 0, 0

    while i < len(A) and j < len(B):
        a1, a2 = A[i][0], A[i][1]
        b1, b2 = B[j][0], B[j][1]

        c1 = max(A[i][0], B[j][0])
        c2 = min(A[i][1], B[j][1])

        if c2 >= c1:
            res.append([c1, c2])

        if a2 < b2:
            i += 1
        else:
            j += 1
    return res


if __name__ == "__main__":
    A = [[0, 2], [5, 10], [13, 23], [24, 25]]
    B = [[1, 5], [8, 12], [15, 24], [25, 26]]
    print(interval_intersection(A, B))