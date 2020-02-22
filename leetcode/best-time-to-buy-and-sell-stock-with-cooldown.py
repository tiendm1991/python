class Solution:
    def maxProfit(self, p) -> int:
        n = len(p)
        if n < 2:
            return 0
        dp = [[0] * 2 for i in range(n)]
        dp[1][0] = p[1] - p[0] if p[1] > p[0] else 0
        dp[1][1] = dp[1][0]
        for i in range(2, n):
            for j in range(i):
                if p[j] < p[i]:
                    dp[i][0] = max(dp[i][0], p[i] - p[j])
                    if j > 2:
                        dp[i][0] = max(dp[i][0], p[i] - p[j] + dp[j - 2][1])
                dp[i][1] = max(dp[i][0], dp[i-1][1])
        return dp[n-1][1]
s = Solution()
print(s.maxProfit([6,1,3,2,4,7]))
print(s.maxProfit([6,1,3,6,4,0,2,3]))
