class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        _max = 10 ** 9 + 7
        m, n = len(dungeon), len(dungeon[0])
        dp = [[_max if i == m or j == n else 0 for j in range(n + 1)] for i in range(m + 1)]
        dp[m - 1][n], dp[m][n - 1] = 1, 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # right = max(dp[i][j + 1] - dungeon[i][j], 1)
                # down = max(dp[i + 1][j] - dungeon[i][j], 1)
                # dp[i][j] = min(right, down)
                dp[i][j] = max(min(dp[i][j + 1], dp[i + 1][j]) - dungeon[i][j], 1)
        return dp[0][0]


s = Solution()
# print(s.calculateMinimumHP([[-2, -3, 3],
#                             [-5, -10, 1],
#                             [10, 30, -5]]))
print(s.calculateMinimumHP([[0, -74, -47, -20, -23, -39, -48],
                            [37, -30, 37, -65, -82, 28, -27],
                            [-76, -33, 7, 42, 3, 49, -93],
                            [37, -41, 35, -16, -96, -56, 38],
                            [-52, 19, -37, 14, -65, -42, 9],
                            [5, -26, -30, -65, 11, 5, 16],
                            [-60, 9, 36, -36, 41, -47, -86],
                            [-22, 19, -5, -41, -8, -96, -95]]))
