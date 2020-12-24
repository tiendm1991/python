import math
import collections


class Solution:
    def largestComponentSize(self, a) -> int:
        a.sort()
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

        for x in range(2, max_num + 1):
            first = -1
            for i, num in enumerate(a):
                if num % x == 0:
                    if first == -1:
                        first = i
                    else:
                        union(first, i)
        d = collections.Counter(p)
        return max([d[k] for k in d])


s = Solution()
print(s.largestComponentSize([2, 3, 4, 6, 7, 12, 21, 39]))
# print(s.largestComponentSize([4, 6, 15, 35]))
# print(s.largestComponentSize([20, 50, 9, 63]))
