class Solution:
    def minCostConnectPoints(self, points) -> int:
        n = len(points)
        if n == 1:
            return 0
        edges = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                edges.append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j))
        edges = sorted(edges, key=lambda x: x[0])

        p = [i for i in range(n)]

        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            if x < y:
                p[y] = x
            else:
                p[x] = y

        ans = 0
        for cost, i, j in edges:
            u, v = find(i), find(j)
            if u != v:
                ans += cost
                union(u, v)

        return ans


s = Solution()
print(s.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
