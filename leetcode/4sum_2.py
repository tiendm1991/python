import collections


class Solution:
    def fourSumCount(self, a, b, c, d) -> int:
        x = collections.Counter([xa + xb for xb in b for xa in a])
        y = collections.Counter([xc + xd for xd in d for xc in c])
        res = 0
        for xx in x:
            if -xx in y:
                res += x[xx] * y[-xx]
        return res


s = Solution()
print(s.fourSumCount([1, 2],
                     [-2, -1],
                     [-1, 2],
                     [0, 2]))
