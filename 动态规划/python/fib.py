def helper(l, n):
    if n == 1 or n == 2:
        return 1
    if l[n] != 0:
        return l[n]
    l[n] = helper(l, n-1) + helper(l, n-2)
    return l[n]


def fib1(N):
    if N < 1:
        return 0
    l = [0] * (N + 1)
    return helper(l, N)


def fib2(N):
    if N == 1 or N == 2:
        return 1
    pre = 1
    succ = 1
    sum = pre + succ
    for i in range(3, N):
        pre = succ
        succ = sum
        sum = pre + succ
    return sum


if __name__ == "__main__":
    print(fib2(10))