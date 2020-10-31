class Solution:
    def new21Game(self, n: int, k: int, w: int) -> float:
        if n == 0 or n >= k + w - 1:
            return 1
        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        preSum = [0] * (n + 1)
        preSum[0] = 1.0
        for i in range(1, n + 1):
            if i <= k and i <= w:
                dp[i] = preSum[i - 1] / w
            else:
                # for j in range(1, w + 1):
                #     if 0 <= i - j < k:
                #         dp[i] += dp[i - j] / w
                dp[i] = preSum[min(k, i) - 1]
                if i > w:
                    dp[i] -= preSum[i - w - 1]
                dp[i] /= w
            preSum[i] = preSum[i - 1] + dp[i]
        return sum(dp[k:])


s = Solution()
print(s.new21Game(4, 3, 5))
print(s.new21Game(21, 17, 10))
