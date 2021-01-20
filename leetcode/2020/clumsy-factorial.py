class Solution:
    def clumsy(self, n: int) -> int:
        res = 0
        while n > 0:
            flag = -1
            if res == 0:
                flag = 1
            if n >= 4:
                res = res + flag * (n * (n - 1) // (n - 2)) + (n - 3)
                n -= 4
            elif n == 3:
                res = res + flag * (n * (n - 1) // (n - 2))
                n -= 3
            elif n == 2:
                res = res + flag * (n * (n - 1))
                n -= 2
            else:
                res = res + flag * n
                n -= 1
        return res


s = Solution()
print(s.clumsy(4))
print(s.clumsy(10))
