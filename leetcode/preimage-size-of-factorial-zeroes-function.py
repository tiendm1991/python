class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        color = [0] * n
        cycles = set()

        def dfs(u, p):
            color[u] = 1
            p.append(u)
            for v in graph[u]:
                if v == u:
                    for x in p:
                        cycles.add(x)
                elif color[v] == 0:
                    dfs(v, p)
                elif color[v] == 1 or (v in cycles and color[v] == 2):
                    for x in p:
                        cycles.add(x)
            p.pop()
            color[u] = 2
            return

        for i in range(n):
            if color[i] == 0:
                dfs(i, [])
        ans = []
        for i in range(n):
            if i not in cycles:
                ans.append(i)
        return ans


s = Solution()
print(s.eventualSafeNodes([[2, 3], [2, 3, 4], [3, 4], [], [1]]))
print(s.eventualSafeNodes([[1, 2, 3, 4], [1, 2, 3, 4], [3, 4], [4], []]))
print(s.eventualSafeNodes([[0], [2, 3, 4], [3, 4], [0, 4], []]))
print(s.eventualSafeNodes([[1, 2, 5], [2, 3], [4], [0], [], [6], [0]]))
print(s.eventualSafeNodes([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]))
