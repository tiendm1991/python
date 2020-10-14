class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def trailingZero(x):
            a = 5
            ans = 0
            while x >= a:
                ans += x // a
                a *= 5
            return ans

        l, r = 0, 5 * 10 ** 9
        while l <= r:
            m = (l + r) // 2
            t = trailingZero(m)
            if t < k:
                l = m + 1
            elif t > k:
                r = m - 1
            else:
                return 5
        return 0


s = Solution()
print(s.preimageSizeFZF(5))
print(s.preimageSizeFZF(11))
print(s.preimageSizeFZF(12))
