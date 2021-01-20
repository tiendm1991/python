import math


class Solution:
    def numMusicPlaylists(self, n: int, l: int, k: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0 for j in range(l + 1)] for i in range(n + 1)]
        for i in range(k + 1, n + 1):
            for j in range(i, l + 1):
                if i == j or i == k + 1:
                    dp[i][j] = math.factorial(i) % mod
                else:
                    dp[i][j] = (dp[i - 1][j - 1] * i + dp[i][j - 1] * (i - k)) % mod
        return dp[n][l]


s = Solution()
print(s.numMusicPlaylists(3, 3, 1))
print(s.numMusicPlaylists(2, 3, 0))
