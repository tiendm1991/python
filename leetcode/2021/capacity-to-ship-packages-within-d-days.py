class Solution:
    def shipWithinDays(self, weights, D: int) -> int:
        s = sum(weights)
        n = len(weights)
        l, r = max(weights), s

        def count(x):
            res = 1
            i, cur = 0, 0
            while i < n:
                if cur + weights[i] > x:
                    cur = 0
                    res += 1
                cur += weights[i]
                i += 1
            return res <= D

        while l < r:
            m = (l + r) // 2
            if count(m):
                r = m
            else:
                l = m + 1
        return l


s = Solution()
print(s.shipWithinDays([1, 2, 3, 1, 1], 4))
# print(s.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
