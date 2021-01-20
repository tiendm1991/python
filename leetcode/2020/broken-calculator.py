class Solution:
    def brokenCalc(self, x: int, y: int) -> int:
        res = 0
        while y > x:
            res += 1
            if y % 2 == 0:
                y //= 2
            else:
                y += 1
        res += x - y
        return res


s = Solution()
print(s.brokenCalc(2, 5))
print(s.brokenCalc(3, 5))
print(s.brokenCalc(3, 10))
print(s.brokenCalc(68, 71))
print(s.brokenCalc(1, 10))
print(s.brokenCalc(5, 8))
print(s.brokenCalc(1000000000, 1))
