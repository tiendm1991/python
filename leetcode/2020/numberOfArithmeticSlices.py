import functools
from datetime import datetime, time
import math
import bisect
import random
import collections


class Solution:
    def numberOfArithmeticSlices(self, a) -> int:
        n = len(a)
        dp1 = [{0: 1} for i in range(n)]
        dp2 = [{0: 1} for i in range(n)]
        dp3 = [{0: 1} for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                x = a[i] - a[j]
                if x in dp1[j]:
                    dp1[i][x] = dp1[j][x] + 1
                else:
                    dp1[i][x] = 2
                dp3[i][x] = dp3[i].get(x, 0) + 1
                dp2[i][x] = dp2[i].get(x, 0) + (dp2[j].get(x, 0) + 1)
        s = 0
        for i in range(n):
            s1 = dp1[i]
            for k in s1:
                if s1[k] < 3:
                    continue
                if k == 0:
                    s += pow(2, s1[k] - 1) - s1[k]
                else:
                    s += dp2[i][k] - dp3[i][k]
        return s


s = Solution()
startTime = datetime.now()
print(s.numberOfArithmeticSlices([2, 2, 2, 2]))
print(datetime.now() - startTime)
