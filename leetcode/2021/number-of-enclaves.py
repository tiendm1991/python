class Solution:
    def numEnclaves(self, a) -> int:
        m, n = len(a), len(a[0])

        def dfs(x, y):
            a[x][y] = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i * j == 0 and i + j != 0 and 0 <= x + i < m and 0 <= y + j < n and a[x + i][y + j] == 1:
                        dfs(x + i, y + j)

        for i in range(m):
            if a[i][0] == 1:
                dfs(i, 0)
            if a[i][n - 1] == 1:
                dfs(i, n - 1)
        for j in range(n):
            if a[0][j] == 1:
                dfs(0, j)
            if a[m - 1][j] == 1:
                dfs(m - 1, j)
        return sum([sum(r) for r in a])


s = Solution()
print(s.numEnclaves([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))
