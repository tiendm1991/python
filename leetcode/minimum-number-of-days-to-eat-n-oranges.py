class Solution:
    def minDays1(self, n: int) -> int:
        dp = [0] * (n + 1)
        if n == 1:
            return 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = 1 + min(i % 3 + dp[i // 3], i % 2 + dp[i // 2])
        return dp[n]
        dp = {0: 0, 1: 1}


def minDays(self, n: int) -> int:
    dp = {0: 0, 1: 1}

    def f(x):
        if x in dp:
            return dp[x]
        ans = 1 + min(x % 3 + f(x // 3), x % 2 + f(x // 2))
        dp[x] = ans
        return dp[x]

    return f(n)


s = Solution()
print(s.minDays(6))
print(s.minDays(10))
print(s.minDays(9459568))
