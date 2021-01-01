import math


class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        dp = {1: 1}

        def helper(t):
            if t in dp:
                return dp[t]
            a = int(math.log(t, x))
            if 0 <= math.pow(x, a) - t < 0.001:
                return a - 1
            res = t * 2
            res = 2 + helper(t - 1) if a == 0 else a + helper(t - x ** a)
            if x ** (a + 1) - t < t:
                res = min(res, a + 1 + helper(x ** (a + 1) - t))
            dp[t] = res
            return res

        return helper(target)


s = Solution()
print(s.leastOpsExpressTarget(3, 19))
print(s.leastOpsExpressTarget(5, 501))
print(s.leastOpsExpressTarget(100, 100000000))
print(s.leastOpsExpressTarget(11, 5041))
print(s.leastOpsExpressTarget(11, 50041))
