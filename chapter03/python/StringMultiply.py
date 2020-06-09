def string_multiply(s1, s2):
    m = len(s1)
    n = len(s2)
    res = [0] * (m+n)
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            res_ij = int(s1[i]) * int(s2[j])
            p1 = res_ij // 10
            p2 = res_ij % 10
            if res[i+j+1] + p2 > 9:
                res[i+j] += 1
            res[i + j + 1] = (res[i + j + 1] + p2) % 10

            if res[i+j] + p1 > 9:
                res[i+j-1] += 1
            res[i + j] = (res[i + j] + p1) % 10

    s = ""
    for e in res:
        if e != 0:
            s += str(e)
    return s


def string_multiply_simplify(s1, s2):
    m = len(s1)
    n = len(s2)
    res = [0] * (m+n)
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            p1 = i + j
            p2 = i + j + 1
            mul = int(s1[i]) * int(s2[j])
            s = mul + res[p2]
            res[p1] += s // 10
            res[p2] = s % 10

    s = ""
    for e in res:
        if e != 0:
            s += str(e)
    return s


if __name__ == "__main__":
    s1 = "123"
    s2 = "45"
    print(string_multiply_simplify(s1, s2))