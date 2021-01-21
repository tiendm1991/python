class Solution:
    def baseNeg2_2(self, n: int) -> str:
        if n == 0:
            return "0"
        res = ""
        b = -2
        while n != 0:
            m = n % b
            res = str(-m) + res
            n = (n + m) // b
        return res

    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        res = ""
        b = -2
        while n != 0:
            m = abs(n % b)
            res = str(m) + res
            n = (n - m) // b
        return res


s = Solution()
print(s.baseNeg2(2))
print(s.baseNeg2(3))
