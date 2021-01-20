class Solution:
    def loudAndRich(self, richer, quiet):
        n = len(quiet)
        edges = {i: [] for i in range(n)}
        for e in richer:
            edges[e[1]].append(e[0])
        ans = [-1] * n

        def dfs(u):
            ans[u] = u
            for v in edges[u]:
                x = ans[v]
                if x == -1:
                    x = dfs(v)
                if quiet[x] < quiet[ans[u]]:
                    ans[u] = x
            return ans[u]

        for i in range(n):
            dfs(i)
        return ans


s = Solution()
print(s.loudAndRich([[0, 2], [1, 2]], [0, 1, 2]))
print(s.loudAndRich([[0, 1]], [0, 1]))
print(s.loudAndRich([[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]],
                    [3, 2, 5, 4, 6, 1, 7, 0]))
