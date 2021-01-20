import functools
from datetime import datetime, time
import math
import random


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        MAX_INTEGER = float('inf')
        dp = [[MAX_INTEGER for j in range(n + 1)] for i in range(n + 1)]
        for i in range(n, 0, -1):
            for j in range(i, n + 1):
                if i == j:
                    dp[i][j] = 0
                elif j - i == 1:
                    dp[i][j] = i
                elif j - i == 2:
                    dp[i][j] = (i + j) // 2
                else:
                    for k in range((i + j) // 2, j):
                        dp[i][j] = min(dp[i][j], k + max(dp[k + 1][j], dp[i][k - 1]))
        return dp[1][n]


s = Solution()
startTime = datetime.now()
print(s.getMoneyAmount(17))
print(datetime.now() - startTime)
