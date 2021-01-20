class Solution:
    def maxProfit(self, a) -> int:
        if not a:
            return 0
        a = [a[0] + 1] + a + [a[-1] - 1]
        n = len(a)
        if n < 4:
            return 0
        d1, d2 = [0] * n, [0] * n
        m1, m2 = a[1], a[-2]
        for i in range(2, n):
            d1[i] = d1[i - 1]
            if a[i] > m1:
                d1[i] = max(d1[i], a[i] - m1)
            else:
                m1 = a[i]
        for i in range(n - 3, -1, -1):
            d2[i] = d2[i + 1]
            if a[i] < m2:
                d2[i] = max(d2[i], m2 - a[i])
            else:
                m2 = a[i]
        ans = 0
        for i in range(1, n - 1):
            ans = max(ans, d1[i] + d2[i + 1])
        return ans


s = Solution()
print(s.maxProfit([2, 1, 2, 1, 0, 0, 1]))
