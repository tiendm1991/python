class Solution:
    def maxProductPath(self, grid) -> int:
        mod = 10 ** 9 + 7
        rows = len(grid)
        if rows == 0:
            return -1
        cols = len(grid[0])
        dp = [[[1, -1] for j in range(cols)] for i in range(rows)]
        zero = -1
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    zero = 0
                if i == 0 and j == 0:
                    if grid[i][j] < 0:
                        dp[i][j][0] = grid[i][j]
                        dp[i][j][1] = -1
                    else:
                        dp[i][j][0] = 1
                        dp[i][j][1] = grid[i][j]
                    continue
                if j > 0:
                    if grid[i][j] < 0:
                        dp[i][j][0] = grid[i][j] * dp[i][j - 1][1] if dp[i][j - 1][1] != -1 else 1
                        dp[i][j][1] = grid[i][j] * dp[i][j - 1][0] if dp[i][j - 1][0] != 1 else -1
                    else:
                        dp[i][j][0] = grid[i][j] * dp[i][j - 1][0] if dp[i][j - 1][0] != 1 else 1
                        dp[i][j][1] = grid[i][j] * dp[i][j - 1][1] if dp[i][j - 1][1] != -1 else -1
                if i > 0:
                    if grid[i][j] < 0:
                        dp[i][j][0] = min(dp[i][j][0], grid[i][j] * dp[i - 1][j][1] if dp[i - 1][j][1] != -1 else 1)
                        dp[i][j][1] = max(dp[i][j][1], grid[i][j] * dp[i - 1][j][0] if dp[i - 1][j][0] != 1 else -1)
                    else:
                        dp[i][j][0] = min(dp[i][j][0], grid[i][j] * dp[i - 1][j][0] if dp[i - 1][j][0] != 1 else 1)
                        dp[i][j][1] = max(dp[i][j][1], grid[i][j] * dp[i - 1][j][1] if dp[i - 1][j][1] != -1 else -1)
                dp[i][j][0] = dp[i][j][0]
                dp[i][j][1] = dp[i][j][1]
        ans = max(dp[rows - 1][cols - 1][1], zero)
        if ans == -1:
            return ans
        return ans % mod


s = Solution()
print(s.maxProductPath([[1, -2, 1], [1, -2, 1], [3, -4, 1]]))
