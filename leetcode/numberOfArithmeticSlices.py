import functools
from datetime import datetime, time
import math
import bisect
import random
import collections


class Solution:
    def numberOfArithmeticSlices(self, a) -> int:
        n = len(a)
        dp = [{0:1} for i in range(n)]
        dp2 = [{0:1} for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                x = a[i] - a[j]
                if x in dp[j]:
                    dp[i][x] = dp[j][x] + 1
                else:
                    dp[i][x] = 2
                dp2[i][x] = dp2[i].get(x, 0) +  dp2[j].get(x, 1)
        s = 0
        for i, _set in enumerate(dp):
            for k in _set:
                if _set[k] < 3:
                    continue
                n = _set[k]
                s += (n - 2) * dp2[i][k]
        return s

s = Solution()
startTime = datetime.now()
print(s.numberOfArithmeticSlices([2,2,3,4,5]))
print(datetime.now() - startTime)

