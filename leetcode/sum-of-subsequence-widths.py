class Solution:
    def sumSubseqWidths(self, a) -> int:
        mod = 10 ** 9 + 7
        n = len(a)
        if n == 1:
            return 0
        a.sort()
        res = 0
        for i in range(1, n):
            for j in range(i):
                res = (res + (a[i] - a[j]) * (2 ** (i - j - 1))) % mod
        return res


s = Solution()
print(s.sumSubseqWidths([1, 3, 4, 6, 9]))
print(s.sumSubseqWidths([1, 2, 3, 4, 5]))
