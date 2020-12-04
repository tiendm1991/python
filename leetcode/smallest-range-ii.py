class Solution:
    def smallestRangeII(self, a, k: int) -> int:
        n = len(a)
        if n == 1:
            return 0
        a.sort()
        res = a[-1] - a[0]
        mi, ma = a[1], a[-1]
        for i in range(n - 1):
            x = a[i] + 2 * k
            if x > ma:
                res = min(res, x - mi)
                ma = x
                mi = a[i + 1]
            elif x < mi:
                res = min(res, ma - x)
                mi = min(a[i + 1], mi)
            else:
                mi = a[i + 1]
        return res


s = Solution()
print(s.smallestRangeII([1, 3, 6], 3))
