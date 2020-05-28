import List


class Solution:
    # 121. 买卖股票的最佳时机
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        dp = [0] * len(prices)
        minprice = prices[0]

        for i in range(1, len(prices)):
            minprice = min(minprice, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - minprice)

        return dp[-1]


class Solution:
    # 121. 买卖股票的最佳时机
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        minprice = prices[0]
        profit = 0
        for i in range(n):
            profit = max(profit, prices[i] - minprice)
            minprice = min(minprice, prices[i])
        return profit


class Solution:
    # 122. 买卖股票的最佳时机 II
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        dp = [[None, None] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        return dp[-1][0]

# 123. 买卖股票的最佳时机 III


# 188. 买卖股票的最佳时机 IV

class Solution:
    # 309. 最佳买卖股票时机含冷冻期
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        dp = [[None, None] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
        dp[1][1] = max(dp[0][1], -prices[1])

        for i in range(2, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])

        return dp[-1][0]


class Solution:
    # 714. 买卖股票的最佳时机含手续费
    def maxProfit(self, prices: List[int], free: int) -> int:
        n = len(prices)
        if n < 2:
            return 0

        dp = [[None, None] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i]-free)
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])

        return dp[-1][0]