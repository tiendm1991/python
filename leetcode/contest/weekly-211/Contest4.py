import math


class Solution:
    def areConnected(self, n: int, threshold: int, queries):
        m = len(queries)
        ans = [False] * m
        if threshold == 0:
            return [True] * m
        if threshold == n:
            return [False] * m

        def check(a, b):
            g = math.gcd(a, b)
            if g <= threshold:
                return False
            return True

        p = [0 if i <= threshold else i for i in range(n + 1)]

        def find(a):
            if a != p[a]:
                p[a] = find(p[a])
            return p[a]

        for x in range(threshold + 1, n + 1):
            for y in range(x * 2, n + 1, x):
                rx, ry = find(x), find(y)
                if rx > 0 and ry > 0:
                    if rx <= ry:
                        p[ry] = rx
                    else:
                        p[rx] = ry

        for i, q in enumerate(queries):
            a, b = find(q[0]), find(q[1])
            if a > 0 and b > 0 and a == b:
                ans[i] = True
        return ans


s = Solution()
print(s.areConnected(26, 3, [[16, 9]]))
