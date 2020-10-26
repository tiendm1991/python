class Solution:
    def minTime(self, n: int, edges, hasApple) -> int:
        count = 0
        path = []
        d = {e[1]: e[0] for e in edges}

        def trace(p, v):
            p.append(v)
            if v == 0:
                return p
            return trace(p, d[v])

        for i in range(n):
            if not hasApple[i]:
                continue
            p = trace([], i)
            path.append(p[::-1])
        i = 1
        m = max([len(p) for p in path] + [0])
        while i < m:
            s = set()
            for p in path:
                if i < len(p):
                    s.add(p[i])
            count += len(s) * 2
            i += 1
        return count


s = Solution()
print(s.minTime(7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
                [False, False, True, False, True, True, False]))
