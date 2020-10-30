class Solution:
    def numMagicSquaresInside(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        if m < 3 or n < 3:
            return 0

        def check(x, y):
            for i in range(3):
                if grid[x + i][y] + grid[x + i][y + 1] + grid[x + i][y + 2] != 15:
                    return 0
                if grid[x][y + i] + grid[x + 1][y + i] + grid[x + 2][y + i] != 15:
                    return 0
            if grid[x][y] + grid[x + 1][y + 1] + grid[x + 2][y + 2] != 15:
                return 0
            if grid[x + 2][y] + grid[x + 1][y + 1] + grid[x][y + 2] != 15:
                return 0
            s = set([grid[a][b] for b in range(y, y + 3) for a in range(x, x + 3)])
            return 1 if len(s) == 9 and min(s) == 1 and max(s) == 9 else 0

        ans = 0
        for i in range(m - 2):
            for j in range(n - 2):
                ans += check(i, j)
        return ans


s = Solution()
print(s.numMagicSquaresInside([[3, 2, 9, 2, 7],
                               [6, 1, 8, 4, 2],
                               [7, 5, 3, 2, 7],
                               [2, 9, 4, 9, 6],
                               [4, 3, 8, 2, 5]]))
print(s.numMagicSquaresInside([[1, 8, 6],
                               [10, 5, 0],
                               [4, 2, 9]]))
print(s.numMagicSquaresInside([[4, 3, 8, 4],
                               [9, 5, 1, 9],
                               [2, 7, 6, 2]]))
