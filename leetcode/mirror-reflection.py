import math


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        g = math.gcd(p, q)
        m, n = q // g, p // g
        if n % 2 == 0:
            return 2
        else:
            return m % 2
        return -1


s = Solution()
print(s.mirrorReflection(3, 2))
