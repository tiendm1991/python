class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def valid(i, j, visited):
            return 0 <= i < m and 0 <= j < n and not visited[i][j] and grid[i][j] == 1

        def dfs(i, j, visited):
            visited[i][j] = True
            if valid(i - 1, j, visited):
                dfs(i - 1, j, visited)
            if valid(i + 1, j, visited):
                dfs(i + 1, j, visited)
            if valid(i, j - 1, visited):
                dfs(i, j - 1, visited)
            if valid(i, j + 1, visited):
                dfs(i, j + 1, visited)

        def count():
            c = 0
            visited = [[False for i in range(n)] for j in range(m)]
            for i in range(m):
                for j in range(n):
                    if not visited[i][j] and grid[i][j] == 1:
                        c += 1
                        dfs(i, j, visited)
            return c

        if count() != 1:
            return 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count() != 1:
                        return 1
                    grid[i][j] = 1
        return 2
