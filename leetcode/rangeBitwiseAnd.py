import math


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0:
            return 0
        if m == n:
            return m
        len_m, len_n = math.log2(m), math.log2(n)
        ceil_m, ceil_n = math.ceil(len_m), math.ceil(len_n)
        len_m = ceil_m if ceil_m > len_m else ceil_m + 1
        len_n = ceil_n if ceil_n > len_n else ceil_n + 1
        if len_m < len_n:
            return 0
        a = int(math.pow(2, len_n - 1))
        return a + self.rangeBitwiseAnd(m - a, n - a)

s = Solution()
print(s.rangeBitwiseAnd(5,7))
print(s.rangeBitwiseAnd(6,7))