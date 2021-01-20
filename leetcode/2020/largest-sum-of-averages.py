class Solution:
    def largestSumOfAverages(self, a, k) -> float:
        n = len(a)
        if k == 1:
            return sum(a) / n
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + a[i - 1]
        dp = [[0.0 for j in range(k + 1)] for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                if j == 1:
                    dp[i][j] = prefix[i] / i
                    continue
                for tmp in range(i - 1, -1, -1):
                    dp[i][j] = max(dp[i][j], dp[tmp][j - 1] + (prefix[i] - prefix[tmp]) / (i - tmp))

        return dp[n][k]


s = Solution()
print(s.largestSumOfAverages([9, 1, 2, 3, 9], 3))
