class Solution:
    def shortestPathLength(self, graph) -> int:
        n = len(graph)
        target = (1 << n) - 1
        if n <= 2:
            return n - 1
        q = []
        visited = set()
        for i in range(n):
            q.append([1 << i, i])
            visited.add((1 << i, i))
        ans = 0
        while q:
            newQ = []
            for cur in q:
                if cur[0] == target:
                    return ans
                for nex in graph[cur[1]]:
                    if (cur[0], nex) not in visited:
                        newQ.append([cur[0] | 1 << nex, nex])
                        visited.add((cur[0] | 1 << nex, nex))
            ans += 1
            q = newQ
        return 0


s = Solution()
print(s.shortestPathLength([[1, 2, 3], [0], [0], [0]]))
