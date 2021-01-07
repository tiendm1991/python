class Solution:
    res = 0

    def uniquePathsIII(self, grid) -> int:
        self.res = 0
        m, n = len(grid), len(grid[0])
        start, end = None, None
        target = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)
                elif grid[i][j] == 0:
                    target += 1

        def backtrack(r, c, path):
            tmp = grid[r][c]
            grid[r][c] = -1
            if (r, c) == end:
                self.res += 1 if path == target + 1 else 0
                grid[r][c] = tmp
                return
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i * j != 0 or i + j == 0:
                        continue
                    r_next, c_next = r + i, c + j
                    if 0 <= r_next < m and 0 <= c_next < n and grid[r_next][c_next] != -1:
                        backtrack(r_next, c_next, path + 1)
            grid[r][c] = tmp
            return

        backtrack(start[0], start[1], 0)
        return self.res


s = Solution()
print(s.uniquePathsIII([[1, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 2, -1]]))
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
# 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
print(s.uniquePathsIII([[1, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 2]]))
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
# 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
# 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
# 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
