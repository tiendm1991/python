import collections


class Solution:
    def distanceLimitedPathsExist_slow(self, n: int, edgeList, queries):
        d = {i: {} for i in range(n)}
        m = len(queries)
        for u, v, dis in edgeList:
            d[u][v] = min(d[u].get(v, float('inf')), dis)
            d[v][u] = min(d[v].get(u, float('inf')), dis)
        res = [False] * m
        for i in range(m):
            u, v, limit = queries[i]
            q = collections.deque()
            q.append(u)
            visited = {u}
            while q:
                x = q.popleft()
                if x == v:
                    res[i] = True
                    break
                for w in d[x]:
                    if d[x][w] < limit and w not in visited:
                        q.append(w)
                        visited.add(w)
        return res

    def distanceLimitedPathsExist(self, n: int, edgeList, queries):
        m = len(queries)
        p = [i for i in range(n)]

        def find(u):
            if u != p[u]:
                p[u] = find(p[u])
            return p[u]

        def union(u, v):
            ru, rv = find(u), find(v)
            if ru < rv:
                p[rv] = ru
            else:
                p[ru] = rv

        def isConnect(u, v):
            return find(u) == find(v)

        edgeList = sorted(edgeList, key=lambda e: e[2])
        s = set()
        edges = []
        for e in edgeList:
            if (e[0], e[1]) not in s:
                edges.append(e)
                s.add((e[0], e[1]))
                s.add((e[1], e[0]))
        res = [False] * m
        queries = sorted([(q, i) for i, q in enumerate(queries)], key=lambda x: x[0][2])
        i = 0
        ne = len(edges)
        for q, idx in queries:
            u, v, limit = q
            while i < ne and edges[i][2] < limit:
                union(edges[i][0], edges[i][1])
                i += 1
            res[idx] = isConnect(u, v)
        return res


s = Solution()
print(s.distanceLimitedPathsExist(3, [[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]],
                                  [[0, 1, 2], [0, 2, 5]]))
print(s.distanceLimitedPathsExist(5, [[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]],
                                  [[0, 4, 14], [1, 4, 13]]))
print(s.distanceLimitedPathsExist(13,
                                  [[9, 1, 53], [3, 2, 66], [12, 5, 99], [9, 7, 26], [1, 4, 78], [11, 1, 62],
                                   [3, 10, 50], [12, 1, 71], [12, 6, 63], [1, 10, 63], [9, 10, 88], [9, 11, 59],
                                   [1, 4, 37], [4, 2, 63], [0, 2, 26], [6, 12, 98], [9, 11, 99], [4, 5, 40], [2, 8, 25],
                                   [4, 2, 35], [8, 10, 9], [11, 9, 25], [10, 11, 11], [7, 6, 89], [2, 4, 99],
                                   [10, 4, 63]],
                                  [[9, 7, 65], [9, 6, 1], [4, 5, 34], [10, 8, 43], [3, 7, 76], [4, 2, 15], [7, 6, 52],
                                   [2, 0, 50], [7, 6, 62], [1, 0, 81], [4, 5, 35], [0, 11, 86], [12, 5, 50], [11, 2, 2],
                                   [9, 5, 6], [12, 0, 95], [10, 6, 9], [9, 4, 73], [6, 10, 48], [12, 0, 91],
                                   [9, 10, 58], [9, 8, 73], [2, 3, 44], [7, 11, 83], [5, 3, 14], [6, 2, 33]]))
