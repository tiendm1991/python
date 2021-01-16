import collections
import math


class Solution:
    res = 0

    def numSquarefulPerms(self, a) -> int:
        self.res = 0
        n = len(a)
        cands = {}
        counter = collections.Counter(a)
        for k1 in counter:
            if k1 not in cands:
                cands[k1] = set()
            for k2 in counter:
                x = k1 + k2
                s = int(math.sqrt(x))
                if s * s == x:
                    cands[k1].add(k2)

        def backtrack(num, length):
            if length == n:
                self.res += 1
                return
            for c in cands[num]:
                if counter[c] > 0:
                    counter[c] -= 1
                    backtrack(c, length + 1)
                    counter[c] += 1

        for x in counter:
            counter[x] -= 1
            backtrack(x, 1)
            counter[x] += 1
        return self.res


s = Solution()
# print(s.numSquarefulPerms([1, 17, 8]))
print(s.numSquarefulPerms([2, 2, 2]))
