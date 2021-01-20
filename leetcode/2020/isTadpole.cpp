def isTadpole(adj):
    n = len(adj)
    if n < 4:
        return False
    edges = {i: [] for i in range(n)}
    count = [0] * 4
    for i in range(n):
        for j in range(n):
            if adj[i][j]:
                edges[i].append(j)
        if len(edges[i]) == 0 or len(edges[i]) > 3:
            return False
        else:
            count[len(edges[i])] += 1
    if not (count[1] == 1 and count[2] >= 2 and count[3] == 1):
        return False
    component = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            component += 1
            dfs(i, visited, edges)
    return component == 1


def dfs(u, visited, edges):
    visited[u] = True
    for v in edges[u]:
        if not visited[v]:
            dfs(v, visited, edges)


print(isTadpole([[False, True, True, False, False],
                 [True, False, False, True, False],
                 [True, False, False, True, False],
                 [False, True, True, False, True],
                 [False, False, False, True, True]]))
