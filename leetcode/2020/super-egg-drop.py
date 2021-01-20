class Solution:
    def superEggDrop_Slow(self, K: int, N: int) -> int:
        dp = [[0 if j == 0 else N + 1 for j in range(N + 1)] for i in range(K + 1)]
        for i in range(1, K + 1):
            for j in range(1, N + 1):
                if i == 1:
                    dp[i][j] = j
                    continue
                if j == 1:
                    dp[i][j] = 1
                    continue
                for f in range(1, j + 1):
                    dp[i][j] = min(dp[i][j], 1 + max(dp[i][j - f], dp[i - 1][f - 1]))
        return dp[K][N]

    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0 if j == 0 else N + 1 for j in range(N + 1)] for i in range(K + 1)]
        for i in range(1, K + 1):
            for j in range(1, N + 1):
                if i == 1:
                    dp[i][j] = j
                    continue
                if j == 1:
                    dp[i][j] = 1
                    continue
                x = N + 1
                l, r = 1, j
                while l < r:
                    m = (l + r) // 2
                    if dp[i][j - m] == dp[i - 1][m - 1]:
                        break
                    elif dp[i][j - m] > dp[i - 1][m - 1]:
                        l = m + 1
                    else:
                        r = m
                m = (l + r) // 2
                dp[i][j] = 1 + max(dp[i][j - m], dp[i - 1][m - 1])
        return dp[K][N]


s = Solution()
print(s.superEggDrop(2, 6))
print(s.superEggDrop(3, 14))
