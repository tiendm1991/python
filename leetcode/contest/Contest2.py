import math
class Solution:
    def closestDivisors(self, num: int):
        a, b = num + 1, num + 2
        x = int(math.ceil(math.sqrt(b)))
        while x > 0:
            if a % x == 0:
                y = a // x
                return [min(x,y), max(x, y)]
            if b % x == 0:
                y = b // x
                return [min(x,y), max(x, y)]
            x -= 1
        return None

s = Solution()
print(s.closestDivisors(999))