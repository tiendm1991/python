class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ca, cb = 'a', 'b'
        if a < b:
            ca, cb = 'b', 'a'
            a, b = b, a
        res = ""
        while a > 0 and b > 0:
            if a > b:
                res += ca * 2
                res += cb
                a -= 2
                b -= 1
            else:
                res += ca
                res += cb
                a -= 1
                b -= 1
        if a > 0:
            res += a * ca
        if b > 0:
            res += b * cb
        return res


s = Solution()
print(s.strWithout3a3b(6, 3))
print(s.strWithout3a3b(4, 1))
