class Solution:
    def numPermsDISequence(self, s: str) -> int:
        mod = 10 ** 9 + 7
        n = len(s)
        if n == 1:
            return 1
        dp = [[1 if i == 0 else 0 for j in range(n + 1)] for i in range(n + 1)]
        for i in range(n):
            if s[i] == 'I':
                cur = 0
                for j in range(n - i):
                    cur = (cur + dp[i][j]) % mod
                    dp[i + 1][j] = cur
            else:
                cur = 0
                for j in range(n - i - 1, -1, -1):
                    cur = (cur + dp[i][j + 1]) % mod
                    dp[i + 1][j] = cur
        return dp[n][0]


s = Solution()
print(s.numPermsDISequence("DID"))
print(s.numPermsDISequence("DIDD"))
