class Solution:
    def regionsBySlashes(self, grid) -> int:
        n = len(grid) * 3
        a = [[1 for j in range(n)] for i in range(n)]
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == '\\':
                    for k in range(3):
                        a[3 * i + k][3 * j + k] = 0
                elif grid[i][j] == '/':
                    for k in range(3):
                        a[3 * i + k][3 * j + 2 - k] = 0

        def dfs(x, y):
            a[x][y] = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i * j == 0 and i + j != 0 and 0 <= x + i < n and 0 <= y + j < n and a[x + i][y + j] == 1:
                        dfs(x + i, y + j)

        comp = 0
        for i in range(n):
            for j in range(n):
                if a[i][j] == 1:
                    comp += 1
                    dfs(i, j)
        return comp


s = Solution()
print(s.regionsBySlashes([" /", "  "]))
print(s.regionsBySlashes(["\\/", "/\\"]))
print(s.regionsBySlashes(["/\\", "\\/"]))
