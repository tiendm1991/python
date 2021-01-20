class Solution:
    def strangePrinter(self, s: str) -> int:
        if len(s) == 0:
            return 0
        a = [s[0]]
        for i in range(1, len(s)):
            if s[i] != a[-1]:
                a.append(s[i])
        n = len(a)
        if n == 1:
            return 1
        dp = [[1 if i == j else n for j in range(n)] for i in range(n)]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
                if a[i] == a[j]:
                    dp[i][j] = min(dp[i][j], 1 + dp[i + 1][j - 1])
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] - 1)

        return dp[0][n - 1]


s = Solution()
print(s.strangePrinter("dacbd"))
print(s.strangePrinter("dacadadcd"))
print(s.strangePrinter("dacbcadadcdb"))
print(s.strangePrinter("adacbc"))
print(s.strangePrinter("bacbcab"))
