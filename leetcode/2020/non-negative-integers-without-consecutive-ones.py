import math


class Solution:
    def findIntegers(self, num: int) -> int:
        if num == 0:
            return 1
        if num == 1:
            return 2
        n = int(math.ceil(math.log(num + 1, 2)))
        dp = [[1 if j == 0 else 0 for j in range(2)] for ji in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
            dp[i][1] = dp[i - 1][0]
        ans = dp[n - 1][0] + dp[n - 1][1]
        num -= 2 ** (n - 1)
        if num >= 2 ** (n - 2):
            return ans + dp[n - 2][0] + dp[n - 2][1]
        else:
            return ans + self.findIntegers(num)


s = Solution()
print(s.findIntegers(14))
