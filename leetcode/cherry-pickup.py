class Solution:
    def cherryPickup(self, grid) -> int:
        n = len(grid)
        dp = [[-1 if (i == 0 and j > 1) or (j == 0 and i > 1) else 0 for i in range(n + 1)] for j in range(n + 1)]
        valid = [[False for j in range(n + 1)] for i in range(n + 1)]
        for i in range(n, 0, -1):
            for j in range(n, 0, -1):
                if grid[i - 1][j - 1] == -1:
                    continue
                if i == n and j == n:
                    valid[i][j] = True
                    continue
                if i + 1 <= n:
                    valid[i][j] = valid[i + 1][j]
                if j + 1 <= n:
                    valid[i][j] |= valid[i][j + 1]
        d = {}
        ans = dp[n][n]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if not valid[i][j] or grid[i - 1][j - 1] == -1 or (dp[i - 1][j] == -1 and dp[i][j - 1] == -1):
                    dp[i][j] = -1
                    continue
                if dp[i - 1][j] >= dp[i][j - 1]:
                    dp[i][j] = dp[i - 1][j] + grid[i - 1][j - 1]
                    d[(i, j)] = (i - 1, j)
                else:
                    dp[i][j] = dp[i][j - 1] + grid[i - 1][j - 1]
                    d[(i, j)] = (i, j - 1)
                path = set()
                cur = (i, j)
                while cur[0] != 0 and cur[1] != 0:
                    path.add(cur)
                    cur = d[cur]
                dp2 = [[-1 if (a == 0 and b > 1) or (b == 0 and a > 1) else 0 for a in range(n + 1)] for b in
                       range(n + 1)]
                for a in range(1, n + 1):
                    for b in range(1, n + 1):
                        if grid[a - 1][b - 1] == -1 or (dp2[a - 1][b] == -1 and dp2[a][b - 1] == -1) or not valid[a][b]:
                            dp2[a][b] = -1
                            continue
                        dp2[a][b] = max(dp2[a - 1][b], dp2[a][b - 1])
                        if (a, b) not in path:
                            dp2[a][b] += grid[a - 1][b - 1]
                ans = max(ans, dp[i][j] + dp2[n][n])
        return ans


s = Solution()
print(s.cherryPickup(
    [[1, 1, -1, 1, 1, 1, 0, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 0, -1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, -1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, -1, 1],
     [1, 1, 1, -1, 0, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1],
     [1, 1, -1, 1, 1, 0, -1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, -1, 1, -1, 1, -1, 1, 1],
     [0, -1, 1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1],
     [1, 1, -1, 1, 1, 1, -1, 1, 1, -1, 1, 1, 1, 1, -1, -1, 1, 1, 1, 1],
     [0, 1, -1, -1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, -1, 1, 1, -1],
     [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, -1, 0, 1, 1, -1, 1],
     [-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
     [-1, -1, -1, -1, 1, 1, -1, 1, -1, 1, -1, -1, 1, 1, 1, -1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, -1, 1],
     [1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, 0, 1, 1],
     [0, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1],
     [1, -1, 1, 1, 1, 1, 1, -1, 1, -1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1],
     [-1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, -1, 0, 1, 1],
     [1, 1, -1, 1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 0, 1],
     [-1, 0, 0, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 0, 1, 1, 1, 1, -1, 1]]))
# print(s.cherryPickup(
#     [[1, 1, 1, 0, 0],
#      [0, 0, 1, 0, 1],
#      [1, 0, 1, 0, -1],
#      [0, 0, 1, 0, 0],
#      [0, 0, 1, 1, 1]]))
