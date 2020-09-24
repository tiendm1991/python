class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        n = len(prices)
        dp = [[0, 0] for i in range(n + 1)]
        dp[1][0] = -prices[0]
        for i in range(2, n + 1):
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i - 1] - fee)
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i - 1])
        return dp[n][1]


s = Solution()
print(s.maxProfit([1, 3, 7, 5, 10, 3, 1, 3, 7, 5, 10], 3))
# 1, 3, 7, 5, 10, 3, 1, 3, 7, 5, 10
# print(s.maxProfit([4, 5, 2, 4, 3, 3, 1, 2, 5, 4], 1))
