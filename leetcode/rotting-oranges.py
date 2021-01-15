class Solution:
    def orangesRotting(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        q = [(i, j) for j in range(n) for i in range(m) if grid[i][j] == 2]
        res = 0
        while q:
            newQ = []
            for x, y in q:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i * j == 0 and i + j != 0 and 0 <= x + i < m and 0 <= y + j < n and grid[x + i][y + j] == 1:
                            newQ.append((x + i, y + j))
                            grid[x + i][y + j] = 2
            if newQ:
                res += 1
            q = newQ

        return -1 if len([1 for j in range(n) for i in range(m) if grid[i][j] == 1]) > 0 else res


s = Solution()
print(s.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
print(s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
