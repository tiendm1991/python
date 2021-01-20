class Solution:
    def sumSubseqWidths_low(self, a) -> int:
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

    def sumSubseqWidths(self, a) -> int:
        mod = 10 ** 9 + 7
        n = len(a)
        if n == 1:
            return 0
        a.sort()
        pre, post = [0] * n, [0] * n
        pre[0], post[-1] = a[0], a[-1]
        for i in range(1, n):
            pre[i] = a[i] + pre[i - 1]
        for i in range(n - 2, -1, -1):
            post[i] = a[i] + post[i + 1]
        res = 0
        for i in range(n - 1):
            res = (res + (2 ** i) * (post[i + 1] - pre[n - i - 2])) % mod
        return res


s = Solution()
print(s.sumSubseqWidths([1, 3, 4, 6, 9]), s.sumSubseqWidths_low([1, 3, 4, 6, 9]))
print(s.sumSubseqWidths([1, 2, 3, 4, 5]), s.sumSubseqWidths_low([1, 2, 3, 4, 5]))
