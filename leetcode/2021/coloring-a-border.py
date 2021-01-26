class Solution:
    def colorBorder(self, grid, r0: int, c0: int, color: int):
        m, n = len(grid), len(grid[0])
        visited = set()
        color0 = grid[r0][c0]
        direct = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(x, y):
            visited.add((x, y))
            if x == 0 or x == m - 1 or y == 0 or y == n - 1 or any(
                    (x + d[0], y + d[1]) not in visited and grid[x + d[0]][y + d[1]] != color0 for d in direct):
                grid[x][y] = color
            for d in direct:
                if 0 <= x + d[0] < m and 0 <= y + d[1] < n and (x + d[0], y + d[1]) not in visited and \
                        grid[x + d[0]][y + d[1]] == color0:
                    dfs(x + d[0], y + d[1])

        dfs(r0, c0)
        return grid


s = Solution()
print(s.colorBorder([[1, 1],
                     [1, 2]], 0, 0, 3))
print(s.colorBorder([[1, 2, 2],
                     [2, 3, 2]], 0, 1, 3))
print(s.colorBorder([[1, 1, 1],
                     [1, 1, 1],
                     [1, 1, 1]], 1, 1, 2))
