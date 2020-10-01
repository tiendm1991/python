class Solution:
    def cherryPickup(self, grid) -> int:
        n = len(grid)
        dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
        d = {}
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if grid[i - 1][j - 1] == -1 or (dp[i - 1][j] == -1 and dp[i][j - 1]) == -1:
                    dp[i][j] = -1
                    continue
                if dp[i - 1][j] >= dp[i][j - 1]:
                    dp[i][j] = dp[i - 1][j] + grid[i - 1][j - 1]
                    d[(i, j)] = (i - 1, j)
                else:
                    dp[i][j] = dp[i][j - 1] + grid[i - 1][j - 1]
                    d[(i, j)] = (i, j - 1)
        if dp[n][n] == -1:
            return 0
        ans = dp[n][n]
        cur = (n, n)
        while cur[0] != 0 and cur[1] != 0:
            i, j = cur[0] - 1, cur[1] - 1
            grid[i][j] = 0
            cur = d[cur]
        dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if grid[i - 1][j - 1] == -1 or (dp[i - 1][j] == -1 and dp[i][j - 1]) == -1:
                    dp[i][j] = -1
                    continue
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i - 1][j - 1]
        ans += dp[n][n]
        return ans


s = Solution()
print(s.cherryPickup(
    [[1, 1, 1, 0, 0],
     [0, 0, 1, 0, 1],
     [1, 0, 1, 0, 0],
     [0, 0, 1, 0, 0],
     [0, 0, 1, 1, 1]]))
