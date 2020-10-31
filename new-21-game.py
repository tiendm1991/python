class Solution:
    def new21Game(self, n: int, k: int, w: int) -> float:
        if n == 0 or n >= k + w - 1:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, min(k, n + 1)):
            if i == k:
                break
