import functools
from datetime import datetime, time
import math


class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z == 0:
            return True
        if x == 0 or y == 0:
            return x + y == z
        if x == y:
            return x == z or y == z or x+y == z
        if x + y <= z:
            return x + y == z
        if x > y:
            x, y = y, x
        def recusive(a):
            if a == z % x:
                return True
            n = y - x + a
            if a == n % x:
                return False
            return recusive(n % x)
        return recusive(y % x)

s = Solution()
startTime = datetime.now()
print(s.canMeasureWater(6,9,1))
print(datetime.now() - startTime)

