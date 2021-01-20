class Solution:
    def minFallingPathSum(self, a) -> int:
        n = len(a)
        MAX_INT = 10 ** 9 + 7
        dp = [[MAX_INT if (j == 0 or j == n + 1) else 0 for j in range(n + 2)] for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = a[i - 1][j - 1] + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1])
        return min(dp[n])


s = Solution()
print(s.minFallingPathSum([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]]))
