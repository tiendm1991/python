import math


class Solution:
    def racecar(self, target: int) -> int:
        dp = {1: 1, 2: 4}

        def help(x):
            if x in dp:
                return dp[x]
            n = math.floor(math.log2(x)) + 1
            if x == 2 ** n - 1:
                return n
            dp[x] = n + 1 + help((2 ** n - 1) - x)
            for i in range(1, n):
                start = 2 ** i - 1
                j = 0
                while start - (2 ** j - 1) > 0:
                    dp[x] = min(dp[x], i + 2 + j + help(x - (start - (2 ** j - 1))))
                    j += 1
            return dp[x]

        return help(target)


s = Solution()
print(s.racecar(10))
print(s.racecar(20))
print(s.racecar(5))
print(s.racecar(4))
print(s.racecar(2))
