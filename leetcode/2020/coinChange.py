import functools
from datetime import datetime, time
import math


class Solution:
    def coinChange(self, coins, amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort()
        n = len(coins)
        dp = [[-1 for j in range(amount + 1)] for i in range(n)]
        for i in range(n):
            coin = coins[i]
            for a in range(1, amount + 1):
                dp[i][a] = dp[i - 1][a]
                if a % coin == 0:
                    dp[i][a] = a // coin
                elif a > coin and dp[i][a - coin] != -1:
                    dp[i][a] = min(dp[i][a], dp[i][a - coin] + 1) if dp[i][a] != -1 else dp[i][a - coin] + 1
        return dp[n - 1][amount]


s = Solution()
startTime = datetime.now()
print(s.coinChange([2, 4, 7], 15))
print(datetime.now() - startTime)
