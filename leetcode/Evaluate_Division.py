class Solution:
    def calcEquation(self, equations, values, queries):
        root = {}
        n, m = len(equations), len(queries)
        for e in equations:
            root[e[0]] = (e[0], 1.0)
            root[e[1]] = (e[1], 1.0)

        def find(u):
            if u not in root:
                return None
            if u != root[u][0]:
                r, v = find(root[u][0])
                root[u] = (r, v * root[u][1])
            return root[u]

        for i in range(n):
            x, y = equations[i][0], equations[i][1]
            rx = find(x)
            ry = find(y)
            root[ry[0]] = (rx[0], rx[1] / ry[1] * values[i])

        ans = [-1] * m
        for i, q in enumerate(queries):
            x, y = q[0], q[1]
            rx, ry = find(x), find(y)
            if rx is None or ry is None or rx[0] != ry[0]:
                continue
            else:
                ans[i] = ry[1] / rx[1]
        return ans


s = Solution()
print(
    s.calcEquation([["a", "b"]], [0.5],
                   [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]))
