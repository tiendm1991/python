class Solution:
    def findBall(self, grid):
        m, n = len(grid), len(grid[0])
        a = [[1 for j in range(3 * n)] for i in range(3 * m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for k in range(3):
                        a[3 * i + k][3 * j + k] = 0
                elif grid[i][j] == -1:
                    for k in range(3):
                        a[3 * i + k][3 * j + 2 - k] = 0

        def bfs(y0):
            q = set()
            for i in range(3):
                if a[0][3 * y0 + i] == 1:
                    q.add((0, 3 * y0 + i))
            while q:
                newQ = set()
                for p in q:
                    if p[0] == 3 * m - 1:
                        return p[1] // 3
                    if (p[0] + 1, p[1]) not in newQ and a[p[0] + 1][p[1]] == 1:
                        newQ.add((p[0] + 1, p[1]))
                        if (p[0] + 1, p[1] - 1) not in newQ and 0 <= p[1] - 1 and a[p[0] + 1][p[1] - 1] == 1:
                            newQ.add((p[0] + 1, p[1] - 1))
                        if (p[0] + 1, p[1] + 1) not in newQ and p[1] + 1 < 3 * n and a[p[0] + 1][p[1] + 1] == 1:
                            newQ.add((p[0] + 1, p[1] + 1))
                q = newQ
            return -1

        res = [-1] * n
        for i in range(n):
            res[i] = bfs(i)
        return res


s = Solution()
print(s.findBall([[-1]]))
print(s.findBall([[1, 1, 1, -1, -1],
                  [1, 1, 1, -1, -1],
                  [-1, -1, -1, 1, 1],
                  [1, 1, 1, 1, -1],
                  [-1, -1, -1, -1, -1]]))
