def coin_change(coins, amount):
    def dp(n):
        if n < 0:
            return -1
        if n == 0:
            return 0
        res = float('inf')
        for c in coins:
            subproblem = dp(n - c)
            if subproblem == -1:
                continue
            res = min(subproblem + 1, res)
        return res if res != float('inf') else -1
    return dp(amount)


def coin_change_memo(coins, amount):
    memo = {}

    def dp(n):
        if n < 0:
            return -1
        if n == 0:
            return 0
        res = float('inf')
        for c in coins:
            subproblem = dp(n - c)
            if subproblem == -1:
                continue
            res = min(subproblem + 1, res)
        if res != float('inf'):
            memo[n] = res
        else:
            memo[n] = -1
        return memo[n]
    return dp(amount)


def coin_change_iteration(coins, amount):
    l = [amount] * (amount+1)
    l[0] = 0
    for i in range(1, amount+1):
        res = l[i]
        for c in coins:
            if i - c < 0:
                continue
            res = min(res, l[i-c] + 1)
        l[i] = res
    return l


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    print(coin_change_iteration(coins, amount))
