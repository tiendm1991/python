class Solution:
    def isBipartite(self, graph) -> bool:
        n = len(graph)
        group = {}

        def dfs(u, color):
            group[u] = color
            for v in graph[u]:
                if v in group:
                    if group[v] == color:
                        return False
                elif not dfs(v, 1 - color):
                    return False
            return True

        for u in range(n):
            if u not in group and not dfs(u, 0):
                return False
        return True


s = Solution()
print(s.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))
print(s.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
