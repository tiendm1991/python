# https://leetcode.com/contest/weekly-contest-210/problems/count-subtrees-with-max-distance-between-cities/
class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges):
        e = {i: [] for i in range(1, n + 1)}
        for i, j in edges:
            e[i].append(j)
            e[j].append(i)

        def dfs(vertexes, visited, maxDiameter, u):
            visited.add(u)
            m1, m2 = 0, 0
            for v in e[u]:
                if v not in vertexes or v in visited:
                    continue
                _maxPath = dfs(vertexes, visited, maxDiameter, v)
                if _maxPath > m1:
                    m2 = m1
                    m1 = _maxPath
                elif _maxPath > m2:
                    m2 = _maxPath
            d_u = m1 + m2 + 1
            if d_u > maxDiameter[0]:
                maxDiameter[0] = d_u
            return m1 + 1

        def diameter(t):
            binary_t = bin(t)[2:].zfill(n)
            v = set()
            start = 0
            for i in range(len(binary_t)):
                if binary_t[i] == '1':
                    v.add(i + 1)
                    if start == 0:
                        start = i + 1
            if len(v) == 1:
                return 0
            d_t = [0]
            visited = set()
            dfs(v, visited, d_t, start)
            if len(visited) < len(v):
                return 0
            return d_t[0] - 1

        ans = [0] * (n - 1)
        for i in range(1, (1 << n) + 1):
            d = diameter(i)
            if d > 0:
                ans[d - 1] += 1
        return ans


s = Solution()
print(s.countSubgraphsForEachDiameter(5, [[1, 2], [1, 5], [2, 4], [3, 5]]))
print(s.countSubgraphsForEachDiameter(4, [[1, 2], [2, 3], [2, 4]]))
print(s.countSubgraphsForEachDiameter(3, [[1, 2], [2, 3]]))
