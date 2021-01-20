class Solution:
    def countSquares_slow(self, matrix) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + matrix[i - 1][j - 1]
        s = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for k in range(1, min(i, j) + 1):
                    c = dp[i][j] - dp[i - k][j] - dp[i][j - k] + dp[i - k][j - k]
                    if c == k * k:
                        s += 1
        return s

    def countSquares_dp(self, matrix) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        result = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == 0:
                    continue
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
                result += dp[i][j]
        return result


s = Solution()
print(s.countSquares_dp([[0, 1, 1, 1],
                         [1, 1, 1, 1],
                         [0, 1, 1, 1]]))
