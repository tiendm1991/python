class Solution:
    def cherryPickup(self, grid) -> int:
        n = len(grid)
        dp = {}

        def help(x1, y1, x2, y2):
            if x1 == y1 == x2 == y2 == n - 1:
                return grid[n - 1][n - 1]
            if (x1, y1, x2, y2) in dp:
                return dp[(x1, y1, x2, y2)]
            a1 = grid[x1][y1]
            a2 = grid[x2][y2]
            if a1 == -1 or a2 == -1:
                return -1
            ans = a1
            if x1 != x2 or y1 != y2:
                ans += a2
            a1, a2, a3, a4 = 0, 0, 0, 0
            if 0 <= x1 + 1 < n and 0 <= x2 + 1 < n:
                a1 = help(x1 + 1, y1, x2 + 1, y2)
            if 0 <= x1 + 1 < n and 0 <= y2 + 1 < n:
                a2 = help(x1 + 1, y1, x2, y2 + 1)
            if 0 <= y1 + 1 < n and 0 <= x2 + 1 < n:
                a3 = help(x1, y1 + 1, x2 + 1, y2)
            if 0 <= y1 + 1 < n and 0 <= y2 + 1 < n:
                a4 = help(x1, y1 + 1, x2, y2 + 1)
            nextStage = max(a1, a2, a3, a4)
            if nextStage == -1:
                dp[(x1, y1, x2, y2)] = -1
                return -1
            ans += nextStage
            dp[(x1, y1, x2, y2)] = ans
            return ans

        res = help(0, 0, 0, 0)
        return max(res, 0)


s = Solution()
print(s.cherryPickup(
    [[1, 1, -1, 1, 1],
     [1, 1, 1, 1, 1],
     [-1, 1, 1, -1, -1],
     [0, 1, 1, -1, 0],
     [1, 0, -1, 1, 0]]))
# print(s.cherryPickup(
#     [[1, 1, 1, 0, 0],
#      [0, 0, 1, 0, 1],
#      [1, 0, 1, 0, -1],
#      [0, 0, 1, 0, 0],
#      [0, 0, 1, 1, 1]]))
