import math


class Solution:
    def soupServings(self, N: int) -> float:
        if N >= 4800:
            return 1
        n = int(math.ceil(N / 25))
        dp = [[1 if i == 0 else 0 for j in range(200)] for i in range(200)]
        dp[0][0] = 0.5
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                a = [1, 1, 0.5, 0]
                if i >= 4:
                    a[0] = dp[i - 4][j]
                if i >= 3:
                    a[1] = dp[i - 3][j - 1]
                if j >= 3:
                    a[3] = dp[i - 1][j - 3]
                a[2] = dp[max(i - 2, 0)][max(j - 2, 0)]
                dp[i][j] = sum(a) * 0.25
        return dp[n][n]


s = Solution()
print(s.soupServings(150))
print(s.soupServings(100))
