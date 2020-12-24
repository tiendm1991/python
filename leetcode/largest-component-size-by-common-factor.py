import math
import collections


class Solution:
    def largestComponentSize(self, a) -> int:
        a = sorted([x for x in a if x > 1])
        n = len(a)
        p = list(range(n))
        max_num = max(a)
        sqrt = int(math.sqrt(max_num))

        def find(u):
            if u != p[u]:
                p[u] = find(p[u])
            return p[u]

        def union(u, v):
            ru, rv = find(u), find(v)
            if ru < rv:
                p[rv] = ru
            elif ru > rv:
                p[ru] = rv
            return

        def getPrime(u):

        d = collections.Counter(p)
        return max([d[k] for k in d])


s = Solution()
print(s.largestComponentSize([11, 19, 30, 31, 39, 83, 99]))
# print(s.largestComponentSize([2, 3, 4, 6, 7, 12, 21, 39]))
# print(s.largestComponentSize([4, 6, 15, 35]))
# print(s.largestComponentSize([20, 50, 9, 63]))
