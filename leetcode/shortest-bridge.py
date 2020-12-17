class Solution:
    def shortestBridge(self, a) -> int:
        n = len(a)
        islands = [[0 for j in range(n)] for i in range(n)]

        def dfs(x, y, c):
            islands[x][y] = c
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i + j != 0 and i * j == 0 and 0 <= x + i < n and 0 <= y + j < n \
                            and a[x + i][y + j] == 1 and islands[x + i][y + j] == 0:
                        dfs(x + i, y + j, c)

        def bfs(x, y):
            q = [(x, y)]
            visited = {(x, y)}
            ans = 0
            while q:
                newQ = []
                for p in q:
                    if islands[p[0]][p[1]] == 1:
                        return ans - 1
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if i + j != 0 and i * j == 0 and 0 <= p[0] + i < n and 0 <= p[1] + j < n \
                                    and islands[p[0] + i][p[1] + j] != 2 and (p[0] + i, p[1] + j) not in visited:
                                visited.add((p[0] + i, p[1] + j))
                                newQ.append((p[0] + i, p[1] + j))
                ans += 1
                q = newQ
            return 2 * n

        color = 1
        for i in range(n):
            for j in range(n):
                if islands[i][j] == 0 and a[i][j] == 1:
                    dfs(i, j, color)
                    color += 1

        res = 2 * n
        for i in range(n):
            for j in range(n):
                if islands[i][j] == 2:
                    res = min(res, bfs(i, j))

        return res


s = Solution()
print(s.shortestBridge([[0, 1, 0],
                        [0, 0, 0],
                        [0, 0, 1]]))
print(s.shortestBridge([[1, 1, 1, 1, 1],
                        [1, 0, 0, 0, 1],
                        [1, 0, 1, 0, 1],
                        [1, 0, 0, 0, 1],
                        [1, 1, 1, 1, 1]]))
