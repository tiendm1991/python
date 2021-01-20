import collections


class Solution:
    def numPairsDivisibleBy60(self, time) -> int:
        b = [x for x in time if x % 60 == 0]
        c = [x for x in time if x % 60 == 30]
        res = len(b) * (len(b) - 1) // 2 + len(c) * (len(c) - 1) // 2
        a = [x % 60 for x in time if x % 60 != 0 and x % 60 != 30]
        d = collections.Counter(a)
        res2 = 0
        for x in d:
            res2 += d[x] * d.get(60 - x, 0)
        return res + res2 // 2


s = Solution()
print(s.numPairsDivisibleBy60([30, 20, 150, 100, 40]))
# print(s.numPairsDivisibleBy60([20, 40]))
