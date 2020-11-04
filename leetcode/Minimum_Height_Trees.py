class Solution:
    def findMinHeightTrees(self, n: int, edges):
        if n == 1:
            return [0]
        d = {i: [] for i in range(n)}
        for e in edges:
            d[e[0]].append(e[1])
            d[e[1]].append(e[0])

        def dfs(u, p, maxH):
            ans, d1, d2, v1, v2 = 0, 0, 0, u, -1
            for v in d[u]:
                if v == p:
                    continue
                height, vLast = dfs(v, u, maxH)
                if height > d1:
                    d1, d2 = height, d1
                    v1, v2 = vLast, v1
                elif height > d2:
                    d2, v2 = height, vLast
            if d2 + d1 + 1 > maxH[0]:
                maxH[0], maxH[1], maxH[2] = d1 + d2 + 1, v1, v2
            return d1 + 1, v1

        def bfs(u, maxH):
            q = [u]
            maxH[u] = 1
            height = 1
            while q:
                height += 1
                newQ = []
                for v in q:
                    for x in d[v]:
                        if maxH[x] == -1:
                            maxH[x] = height
                            newQ.append(x)
                q = newQ

        h = [0, -1, -1]
        dfs(0, -1, h)
        h1, h2 = [-1] * n, [-1] * n
        bfs(h[1], h1)
        bfs(h[2], h2)
        a = [max(h1[i], h2[i]) for i in range(n)]
        ans = [0]
        for i in range(1, n):
            if a[i] < a[ans[0]]:
                ans = [i]
            elif a[i] == a[ans[0]]:
                ans.append(i)
        return ans


s = Solution()
print(s.findMinHeightTrees(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]))
