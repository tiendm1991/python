class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10 ** 9 + 7
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5
        dp = [0] * (n + 1)
        dp[1], dp[2], dp[3] = 1, 2, 5
        for i in range(4, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % mod
        return dp[n]

# Explain
# for n from 3
# dp[n] = dp[n-1] + dp[n-2] + 2dp[n-3] + 2dp[n-4] + ... +  2dp[0]
# => dp[n] = dp[n-1] + dp[n-2] + 2(dp[n-3] + dp[n-4] + ... + dp[0])
# => dp[n-1] = dp[n-2] + dp[n-3] + 2(dp[n-4] + ... + dp[0])
# => dp[n] - dp[n-1] = dp[n-1] + dp[n-3]
# => dp[n] = 2dp[n-1] + dp[n-3]
