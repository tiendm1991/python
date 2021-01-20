class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7

        # dp = [[-1 for j in range(k + 1)] for i in range(n + 1)]
        def recursive(n, k):
            if k >= n:
                return 0
            if k == n - 1:
                return 1
            if k == 1:
                return (n - 1) * n // 2
            if dp[n][k] != -1:
                return dp[n][k]
            ans = recursive(n - 1, k)
            for i in range(1, n - k + 1):
                ans = (ans + recursive(n - i, k - 1)) % mod
            dp[n][k] = ans
            return ans

        dp = [[0 for j in range(k + 1)] for i in range(n + 1)]
        prefix = [[0 for j in range(k + 1)] for i in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(1, k + 1):
                if j >= i:
                    break
                if j == i - 1:
                    dp[i][j] = 1
                    prefix[i][j] = prefix[i - 1][j] + dp[i][j]
                    break
                if j == 1:
                    dp[i][j] = (i - 1) * i // 2
                    prefix[i][j] = prefix[i - 1][j] + dp[i][j]
                    continue
                dp[i][j] = dp[i - 1][j]
                # Basic: Slow
                # sum(dp[tmp][j - 1]) with tmp in range[j, i-1]
                # for tmp in range(j, i):
                #     dp[i][j] = (dp[i][j] + dp[tmp][j - 1]) % mod

                # Optimization:
                # using prefix to store sum
                # => sum(dp[tmp][j - 1]) = prefix[i-1][j-1] - prefix[j-1][j-1]
                dp[i][j] = (dp[i][j] + prefix[i - 1][j - 1] - prefix[j - 1][j - 1]) % mod
                prefix[i][j] = prefix[i - 1][j] + dp[i][j]
        return dp[n][k]


s = Solution()
print(s.numberOfSets(4, 2))
print(s.numberOfSets(5, 3))
print(s.numberOfSets(30, 7))
print(s.numberOfSets(751, 201))
