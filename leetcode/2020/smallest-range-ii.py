class Solution:
    def smallestRangeII(self, a, k: int) -> int:
        n = len(a)
        if n == 1:
            return 0
        a.sort()
        res = a[-1] - a[0]
        mn, mx = a[1], a[-1]
        minmin = a[0] + 2 * k
        for i in range(n - 1):
            mn = min(a[i + 1], minmin)
            x = a[i] + 2 * k
            if x <= mn:
                res = min(res, mx - x)
                break
            if x >= mx:
                mx = x
            res = min(res, mx - mn)
        return res


s = Solution()
print(s.smallestRangeII([1, 3, 6], 3))
print(s.smallestRangeII([1, 3, 10], 4))
print(s.smallestRangeII([1, 8, 15, 17], 3))
