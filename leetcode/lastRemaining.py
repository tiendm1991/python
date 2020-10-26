import functools
from datetime import datetime, time
import math
import random


class Solution:
    def lastRemaining(self, n: int) -> int:
        leftToRight = True
        start, end, u = 1, n, 1
        while start < end:
            n = (end - start) // u + 1
            if n % 2 == 1:
                start += u
                end -= u
            elif leftToRight:
                start += u
            else:
                end -= u
            u *= 2
            leftToRight = not leftToRight
        return start


s = Solution()
startTime = datetime.now()
print(s.lastRemaining(100))
print(datetime.now() - startTime)
