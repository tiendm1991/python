class Solution:
    def checkWays(self, pairs) -> int:
        g = {}
        for p in pairs:
            if p[0] not in g:
                g[p[0]] = {p[1]}
            else:
                g[p[0]].add(p[1])
            if p[1] not in g:
                g[p[1]] = {p[0]}
            else:
                g[p[1]].add(p[0])

        def dfs(visited, comps, v, c):
            visited.add(v)
            comps[c].add(v)
            for next_v in g[v]:
                if next_v not in visited:
                    dfs(visited, comps, next_v, c)

        def helper(nodes):
            m = len(nodes) - 1
            if m == 0:
                return 1

            roots = [v for v in nodes if len(g[v]) == m]
            if len(roots) == 0:
                return 0
            r = roots[0]
            for v in g[r]:
                g[v].remove(r)
            comps = {}
            c = 0
            visited = set()
            for v in nodes:
                if v != r and v not in visited:
                    comps[c] = set()
                    dfs(visited, comps, v, c)
                    c += 1
            candidates = {helper(comps[i]) for i in comps}
            if 0 in candidates:
                return 0
            if 2 in candidates:
                return 2
            if len(roots) >= 2:
                return 2
            return 1

        return helper(g.keys())


s = Solution()
print(s.checkWays([[1, 2], [2, 3]]))
print(s.checkWays([[1, 2], [2, 3], [1, 3]]))
