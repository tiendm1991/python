from datetime import datetime


class Solution:
    def updateMatrix(self, matrix):
        m = len(matrix)
        if m == 0:
            return matrix
        n = len(matrix[0])
        dp = [[m + n for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                if i - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
                if j - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                if i + 1 < m:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
                if j + 1 < n:
                    dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)
        return dp


s = Solution()
startTime = datetime.now()
print(s.updateMatrix([[0, 0, 0],
                      [0, 1, 0],
                      [1, 1, 1]]))
print(datetime.now() - startTime)
