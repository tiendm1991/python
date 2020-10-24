class Solution:
    def largestIsland(self, grid) -> int:
        n = len(grid)

        mask = [[0 for i in range(n)] for j in range(n)]
        areas = {}

        def valid(r, c):
            return 0 <= r < n and 0 <= c < n and mask[r][c] == 0 and grid[r][c] == 1

        def valid2(r, c):
            return 0 <= r < n and 0 <= c < n and grid[r][c] == 1

        def dfs(x, y, m):
            mask[x][y] = m
            areas[m] = areas.get(m, 0) + 1
            if valid(x - 1, y):
                dfs(x - 1, y, m)
            if valid(x + 1, y):
                dfs(x + 1, y, m)
            if valid(x, y - 1):
                dfs(x, y - 1, m)
            if valid(x, y + 1):
                dfs(x, y + 1, m)

        color = 1
        for i in range(n):
            for j in range(n):
                if valid(i, j):
                    dfs(i, j, color)
                    color += 1
        if color == 1:
            return 1
        ans = [max(areas.values())]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    continue
                s = set()
                if valid2(i - 1, j):
                    s.add(mask[i - 1][j])
                if valid2(i + 1, j):
                    s.add(mask[i + 1][j])
                if valid2(i, j - 1):
                    s.add(mask[i][j - 1])
                if valid2(i, j + 1):
                    s.add(mask[i][j + 1])
                ans.append(sum([areas[k] for k in s]) + 1)
        return max(ans)


s = Solution()
print(s.largestIsland([[0, 0], [0, 0]]))
