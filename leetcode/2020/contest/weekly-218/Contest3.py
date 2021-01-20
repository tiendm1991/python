class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = 0
        mod = 10 ** 9 + 7
        a = 1
        for x in range(n, 0, -1):
            res = (res + x * a) % mod
            a = a * (2 ** (len("{0:b}".format(x)))) % mod
        return res


s = Solution()
print(s.concatenatedBinary(4))
print(s.concatenatedBinary(12))
