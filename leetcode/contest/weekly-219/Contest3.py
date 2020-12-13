class Solution:
    def stoneGameVII(self, a) -> int:
        n = len(a)
        pre = [0] * (n + 1)
        for i in range(1, n + 1):
            pre[i] = pre[i - 1] + a[i - 1]
        dp = [[[0, 0] for j in range(n)] for i in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j][0] = a[i]
                    continue
                s = pre[j + 1] - pre[i]
                x, y = s - dp[i + 1][j][0], s - dp[i][j - 1][0]
                if x < y:
                    dp[i][j][0] = x
                    dp[i][j][1] = 1
                else:
                    dp[i][j][0] = y
        return dp[1][n - 1][0] if dp[0][n - 1][1] else dp[0][n - 2][0]


s = Solution()
print(s.stoneGameVII([5, 3, 2, 8]), s.stoneGameVII_2([5, 3, 2, 8]))
print(s.stoneGameVII([5, 3, 1, 4, 2]), s.stoneGameVII_2([5, 3, 1, 4, 2]))
