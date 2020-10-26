class Solution:
    def hasValidPath(self, grid) -> bool:
        d1 = {1: [3, 5, 1], 2: [], 3: [], 4: [1, 3, 5], 5: [], 6: [1, 3, 5]}
        d2 = {1: [1, 4, 6], 2: [], 3: [1, 4, 6], 4: [], 5: [1, 4, 6], 6: []}
        d3 = {1: [], 2: [2, 5, 6], 3: [2, 5, 6], 4: [2, 5, 6], 5: [], 6: []}
        d4 = {1: [], 2: [2, 3, 4], 3: [], 4: [], 5: [2, 3, 4], 6: [2, 3, 4]}
        m = len(grid)
        n = len(grid[0])
        visited = [[False for j in range(n)] for i in range(m)]

        def backtrack(r, c):
            if r == m - 1 and c == n - 1:
                return True
            x = grid[r][c]
            if r + 1 < m and not visited[r + 1][c] and grid[r + 1][c] in d3[x]:
                visited[r + 1][c] = True
                if backtrack(r + 1, c):
                    return True
                visited[r + 1][c] = False
            if r - 1 >= 0 and not visited[r - 1][c] and grid[r - 1][c] in d4[x]:
                visited[r - 1][c] = True
                if backtrack(r - 1, c):
                    return True
                visited[r - 1][c] = False
            if c + 1 < n and not visited[r][c + 1] and grid[r][c + 1] in d1[x]:
                visited[r][c + 1] = True
                if backtrack(r, c + 1):
                    return True
                visited[r][c + 1] = False
            if c - 1 >= 0 and not visited[r][c - 1] and grid[r][c - 1] in d2[x]:
                visited[r][c - 1] = True
                if backtrack(r, c - 1):
                    return True
                visited[r][c - 1] = False
            return False

        visited[0][0] = True
        return backtrack(0, 0)


s = Solution()
print(s.hasValidPath([[6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
                      [4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5],
                      [6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
                      [4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5],
                      [6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
                      [4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5],
                      [6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
                      [4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5],
                      [6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
                      [4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5],
                      [6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
                      [4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5],
                      [6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
                      [4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5],
                      [6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3]]))
