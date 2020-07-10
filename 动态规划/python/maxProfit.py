"""
股票买卖问题
对给定一个数组, 它的第i个元素是一支给定股票在第i天的价格. 设计一个算法来计算你所能获得的最大利润. 你最多可以完成k笔交易(一次交易=一次买入+一次卖出).
要求: 不能同时参与多笔交易, 必须在再次购买前出售掉之前的股票

示例:
输入: [2, 4, 1], k=2
输出: 2
解释: 在第一天买入(股票=2), 在第二天卖出(股票=4), 第三天不买, 这样获得的利润为2

dp(dp[i, k, 2])表中: i表示第i天的状态, k表示第i天的交易次数, s=2表示第i天的状态(0表示有股票, 1表示没股票)
base case:
dp[-1, k, 0] = dp[i, 0, 0] = 0
dp[-1, k, 1] = d[i, 0, 1] = -inf

状态转移:
# 第i天, 已经交易了k次, 手中没有股票, 所以在第i-1天就把股票卖了或者在第i天不买不卖
dp[i, k, 0] = max(dp[i-1, k, 1]+prices[i], dp[i-1, k, 0])

# 第i天, 已经交易了k次, 手中有股票, 所以在第i-1天买股票或在第i天不买不卖
dp[i, k, 1] = max(dp[i-1, k-1, 0]-prices[i], dp[i-1, k, 1])

"""
import numpy as np


def max_profit(prices, K):
    """
    该函数为通用框架, 下面函数是针对各情况的简化
    dp表中: i表示第i天的状态, k表示第i天的交易次数, s=2表示第i天的状态(0表示有股票, 1表示没股票)
    约定卖股票时k不变, 买股票时k+=1
    """
    dp = np.zeros((len(prices), K+1, 2))
    for i in range(len(prices)):
        for k in range(0, K+1):
            if i == 0:
                dp[i, k, 0] = 0
                dp[i, k, 1] = -prices[i]
                continue
            if k == 0:
                dp[i, k, 0] = 0
                dp[i, k, 1] = -np.inf
                continue
            # 第i天, 已经交易了k次, 手中没有股票, 所以在第i-1天就把股票卖了或者在第i天不买不卖
            dp[i, k, 0] = max(dp[i-1, k, 1]+prices[i], dp[i-1, k, 0])

            # 第i天, 已经交易了k次, 手中有股票, 所以在第i-1天买股票或在第i天不买不卖
            dp[i, k, 1] = max(dp[i-1, k-1, 0]-prices[i], dp[i-1, k, 1])
    # return int(dp[len(prices)-1, K, 0])
    return dp


def max_profit_k_1(prices):
    n = len(prices)

    dp_i_0 = 0          # dp[-1, k, 0] = 0
    dp_i_1 = -np.inf    # dp[-1, k, 1] = -inf, 还没开始, 所以手中不可能有股票
    for i in range(n):
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
        dp_i_1 = max(dp_i_1, -prices[i])
    return dp_i_0


def max_profit_k_2(prices):
    """
    base case:
    dp[-1, k, 0] = dp[i, 0, 0] = 0
    dp[-1, k, 1] = d[i, 0, 1] = -inf
    """

    n = len(prices)

    dp_i10, dp_i11 = 0, -np.inf     # 交易一次, 手上没股票/有股票
    dp_i20, dp_i21 = 0, -np.inf     # 交易两次, 手上没股票/有股票
    for i in range(n):
        dp_i20 = max(dp_i20, dp_i21+prices[i])
        dp_i21 = max(dp_i21, dp_i10-prices[i])
        dp_i10 = max(dp_i10, dp_i11+prices[i])
        dp_i11 = max(dp_i11, -prices[i])
    return dp_i20


def max_profit_k_inf(prices):
    n = len(prices)
    dp_i_0 = 0
    dp_i_1 = -np.inf
    for i in range(n):
        # tmp = dp_i_0
        dp_i_0 = max(dp_i_1+prices[i], dp_i_0)
        dp_i_1 = max(dp_i_0-prices[i], dp_i_1)
    return dp_i_0


def max_profit_k_inf_with_cooldown(prices):
    """
    每次卖的时候要等一天才能继续交易
    """
    n = len(prices)
    dp_i_0 = 0
    dp_i_1 = -np.inf
    dp_pre_0 = 0
    for i in range(n):
        dp_i_0 = max(dp_i_1+prices[i], dp_i_0)
        dp_i_1 = max(dp_pre_0-prices[i], dp_i_1)
    return dp_i_0


def max_profit_k_inf_with_fee(prices, fee=1):
    """
    每次卖的时候要交手续费
    """
    n = len(prices)
    dp_i_0 = 0
    dp_i_1 = -np.inf
    for i in range(n):
        dp_i_0 = max(dp_i_1+prices[i]-fee, dp_i_0)
        dp_i_1 = max(dp_i_0-prices[i], dp_i_1)
    return dp_i_0


if __name__ == "__main__":
    prices = [3, 2, 6, 5, 0, 3]
    # prices = [1, 2, 3]
    K = 1
    print(max_profit_k_2(prices))
