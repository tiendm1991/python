class Solution:
    def maxSumTwoNoOverlap(self, a, L: int, M: int) -> int:
        n = len(a)

        def helper(l, m):
            left = [0] * n
            pre = 0
            for i in range(n - m):
                pre += a[i]
                if i >= l - 1:
                    left[i] = max(pre, left[i - 1])
                    pre -= a[i - (l - 1)]
            pre = 0
            right = 0
            res = 0
            for i in range(n - 1, l - 2, -1):
                pre += a[i]
                if n - i >= m:
                    right = max(right, pre)
                    res = max(res, right + left[i - 1])
                    pre -= a[i + (m - 1)]
            return res

        return max(helper(L, M), helper(M, L))


s = Solution()
print(s.maxSumTwoNoOverlap([0, 6, 5, 2, 2, 5, 1, 9, 4], 1, 2))
