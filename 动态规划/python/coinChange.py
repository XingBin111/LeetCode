def coin_change(coins, amount):
    def dp(n):
        if n == 0:
            return 0
        if n < 0:
            return -1
        res = float('inf')
        for c in coins:
            subproblem = dp(n - c)
            if subproblem == -1:
                continue
            res = min(res, dp(n - c) + 1)
        return res
    return dp(amount)


def coin_change_dict(coins, amount):
    l = [amount + 1] * (amount + 1)
    l[0] = 0
    for i in range(amount):
        for c in coins:
            if i < c:
                continue
            l[i] = min(l[i - c] + 1, l[i])
    return l[amount]


coins = [1, 2, 5]
amount = 11
print(coin_change(coins, amount))