import functools
from datetime import datetime, time
import math


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [0] * n
        ugly[0] = 1
        i2, i3, i5 = 0, 0, 0
        next_2, next_3, next_5 = 2, 3, 5
        for i in range(1, n):
            next = min(next_2, next_3, next_5)
            ugly[i] = next
            if next == next_2:
                i2 += 1
                next_2 = ugly[i2] * 2
            if next == next_3:
                i3 += 1
                next_3 = ugly[i3] * 3
            if next == next_5:
                i5 += 1
                next_5 = ugly[i5] * 5
        return ugly[n - 1]


s = Solution()
startTime = datetime.now()
print(s.nthUglyNumber(10))
print(datetime.now() - startTime)
