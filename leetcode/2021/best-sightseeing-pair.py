class Solution:
    def maxScoreSightseeingPair(self, a) -> int:
        n = len(a)
        maxi = a[0]
        res = 0
        for idx in range(1, n):
            res = max(res, maxi + a[idx] - idx)
            maxi = max(maxi, a[idx] + idx)
        return res


s = Solution()
print(s.maxScoreSightseeingPair([8, 1, 5, 2, 6]))
