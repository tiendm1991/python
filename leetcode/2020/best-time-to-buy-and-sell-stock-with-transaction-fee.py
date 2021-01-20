class Solution:
    def maxProfit1(self, prices, fee: int) -> int:
        n = len(prices)
        dp = [[0, 0] for i in range(n + 1)]
        dp[1][0] = -prices[0]
        for i in range(2, n + 1):
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i - 1] - fee)
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i - 1])
        return dp[n][1]

    def maxProfit(self, prices, fee: int) -> int:
        n = len(prices)
        buy = [0 for i in range(n)]
        sell = [0 for i in range(n)]
        buy[0] = -prices[0]
        for i in range(1, n):
            sell[i] = max(sell[i - 1], buy[i - 1] + (prices[i] - fee))
            buy[i] = max(buy[i - 1], sell[i - 1] - prices[i])
        return sell[n - 1]


s = Solution()
print(s.maxProfit([1, 3, 7, 5, 10, 3, 1, 3, 7, 5, 10], 3))
# print(s.maxProfit([4, 5, 2, 4, 3, 3, 1, 2, 5, 4], 1))
