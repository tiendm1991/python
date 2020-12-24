import math
import collections


class Solution:
    def largestComponentSize(self, a) -> int:
        if len(a) == 1:
            return 1
        a = sorted([x for x in a if x > 1])
        n = len(a)
        if n == 0:
            return 1
        p = list(range(n))

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

        d = {}
        for idx, x in enumerate(a):
            i = 2
            max_loop = int(math.sqrt(x))
            while i <= max_loop and x > 1:
                if x % i == 0:
                    if i not in d:
                        d[i] = idx
                    else:
                        union(idx, d[i])
                    x //= i
                else:
                    i += 1
            if x > 1:
                if x not in d:
                    d[x] = idx
                else:
                    union(idx, d[x])
        for i in range(n):
            p[i] = find(i)
        counter = collections.Counter(p)
        return max([counter[k] for k in counter])


s = Solution()
print(s.largestComponentSize([11, 19, 30, 31, 39, 83, 99]))
print(s.largestComponentSize([2, 3, 4, 6, 7, 12, 21, 39]))
print(s.largestComponentSize([4, 6, 15, 35]))
print(s.largestComponentSize([20, 50, 9, 63]))
