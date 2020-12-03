class Solution:
    def numPermsDISequence(self, s: str) -> int:
        mod = 10 ** 9 + 7
        n = len(s)
        if n == 1:
            return 1
        dp = [[1 if i == 0 else 0 for j in range(n + 1)] for i in range(n + 1)]
        for i in range(n):
            if s[i] == 'I'
                for j in range(i, n - ):
                    dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % mod
            else:
                for j in range(i):
                    dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % mod
        return dp


s = Solution()
print(s.numPermsDISequence("DID"))
