def construct_next(pat):
    n = len(pat)
    N = [-1] * n

    t = -1
    j = 0
    while j < n - 1:
        if t < 0 or pat[j] == pat[t]:
            t += 1
            j += 1
            N[j] = t
        else:
            t = N[t]
    return N


def construct_next_better(pat):
    n = len(pat)
    N = [-1] * n

    t = -1
    j = 0
    while j < n - 1:
        if t < 0 or pat[j] == pat[t]:
            t += 1
            j += 1
            N[j] = t if pat[j] != pat[t] else N[t]
        else:
            t = N[t]
    return N


def kmp(txt, pat):
    m = len(txt)
    n = len(pat)
    N = construct_next_better(pat)
    print(N)
    i = 0
    j = 0
    while i < m and j < n:
        if j < 0 or txt[i] == pat[j]:
            i += 1
            j += 1
        else:
            j = N[j]
    return i - j


if __name__ == "__main__":
    # pat = "ABABC"
    # txt = "CABAABABAC"

    pat = "000010"
    txt = "0001000010"
    print(kmp(txt, pat))
