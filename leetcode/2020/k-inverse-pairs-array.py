class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0 for i in range(k + 1)] for j in range(n + 1)]
        for i in range(1, n + 1):
            maxK = min(k, i * (i - 1) // 2)
            for j in range(maxK + 1):
                if j == 0:
                    dp[i][j] = 1
                    continue
                # explain:
                # dp[4][0] = dp[3][0] = 1
                # dp[4][1] => 4 at last, last-1                      => dp[4][1] = dp[3][1] + dp[3][0]                       = dp[3][1] + dp[4][0]
                # dp[4][2] => 4 at last, last-1, last - 2            => dp[4][2] = dp[3][2] + dp[3][1] + dp[3][0]            = dp[3][2] + dp[4][1]
                # dp[4][3] => 4 at last, last-1, last - 2, last - 3  => dp[4][3] = dp[3][3] + dp[3][2] + dp[3][1] + dp[3][0] = dp[3][3] + dp[4][2]
                # dp[4][4] => 4 at last, last-1, last - 2, last - 3  => dp[4][4] = dp[3][4] + dp[3][3] + dp[3][2] + dp[3][1] = dp[3][4] + dp[4][3] - dp[3][0]
                # dp[4][5] => 4 at last, last-1, last - 2, last - 3  => dp[4][5] = dp[3][5] + dp[3][4] + dp[3][3] + dp[3][2] = dp[3][5] + dp[4][4] - dp[3][1]
                # dp[4][6] => 4 at last, last-1, last - 2, last - 3  => dp[4][6] = dp[3][6] + dp[3][5] + dp[3][4] + dp[3][3] = dp[3][6] + dp[4][5] - dp[3][2]
                if j < i:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - i]
                dp[i][j] %= mod
        return dp[n][k]


s = Solution()
print(s.kInversePairs(3, 2))
print(s.kInversePairs(3, 3))
print(s.kInversePairs(4, 3))
print(s.kInversePairs(4, 4))
print(s.kInversePairs(10, 4))
