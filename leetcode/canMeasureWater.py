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
            return x == z or y == z or x + y == z
        if x + y <= z:
            return x + y == z
        if x > y:
            x, y = y, x
        return z % math.gcd(x, y) == 0

s = Solution()
startTime = datetime.now()
print(s.canMeasureWater(4, 6, 8))
print(datetime.now() - startTime)

