import functools
import random
import operator
import collections
import queue


def shortestPathWithEdge(start, finish, weight, graph):
    if start == finish:
        return 0
    n = len(graph)
    MAX = 2147483647

    def dijkstra(s, f):
        visited = [False for _ in range(n)]
        dp = [MAX] * n
        dp[s] = 0
        for _ in range(n):
            _min, _minIdx = None, None
            for i, x in enumerate(dp):
                if visited[i]:
                    continue
                if _min == None or x < _min:
                    _min = x
                    _minIdx = i
            if _minIdx == None:
                break
            visited[_minIdx] = True
            for v in range(n):
                if graph[_minIdx][v] != 0:
                    dp[v] = min(dp[v], _min + graph[_minIdx][v])
        return dp

    s, f = min(start, finish) - 1, max(finish, start) - 1
    dp1 = dijkstra(s, f)
    dp2 = dijkstra(f, s)
    _min = dp1[f]
    for i in range(n):
        for j in range(n):
            if i != j and graph[i][j] == 0:
                _min = min(_min, dp1[i] + weight + dp2[j])
    return _min


print(shortestPathWithEdge(2, 1, 10,
                           [[0, 520, 483, 0, 201, 651, 496],
                            [520, 0, 151, 0, 0, 0, 73],
                            [483, 151, 0, 102, 824, 0, 0],
                            [0, 0, 102, 0, 561, 937, 0],
                            [201, 0, 824, 561, 0, 0, 585],
                            [651, 0, 0, 937, 0, 0, 631],
                            [496, 73, 0, 0, 585, 631, 0]]))
