import heapq


class Solution:
    def maxProbability1(self, n: int, edges, succProb, start: int, end: int) -> float:
        d = {i: set() for i in range(n)}
        for i in range(len(succProb)):
            d[edges[i][0]].add((edges[i][1], succProb[i]))
            d[edges[i][1]].add((edges[i][0], succProb[i]))

        def getMaxProbability(p, visited):
            maxPro, maxIdx = 0, 0
            for i in range(n):
                if not visited[i] and p[i] > maxPro:
                    maxPro, maxIdx = p[i], i
            return maxIdx

        visited = [False] * n
        _max = 0
        p = [0] * n
        p[start] = 1
        for _ in range(n):
            v = getMaxProbability(p, visited)
            visited[v] = True
            for adj in d[v]:
                p[adj[0]] = max(p[adj[0]], p[v] * adj[1])
        return p[end]

    def maxProbability(self, n: int, edges, succProb, start: int, end: int) -> float:
        d = {i: set() for i in range(n)}
        for i in range(len(succProb)):
            d[edges[i][0]].add((edges[i][1], succProb[i]))
            d[edges[i][1]].add((edges[i][0], succProb[i]))

        _max = 0
        q = [(-1, start)]
        visited = [False] * n
        while len(q) > 0:
            maxPro = heapq.heappop(q)
            prob, v = -maxPro[0], maxPro[1]
            visited[v] = True
            if v == end:
                return prob
            for adj in d[v]:
                if not visited[adj[0]] and prob * adj[1] > 0:
                    heapq.heappush(q, (-prob * adj[1], adj[0]))
        return 0


s = Solution()
print(s.maxProbability(10, [[0, 3], [1, 7], [1, 2], [0, 9]], [0.31, 0.9, 0.86, 0.36], 2, 3))
