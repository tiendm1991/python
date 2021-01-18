class Solution:
    def canMouseWin(self, grid, catJump: int, mouseJump: int) -> bool:
        m, n = len(grid), len(grid[0])
        direct = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        iCat, iMouse, target = None, None, None
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "M":
                    iMouse = (i, j)
                elif grid[i][j] == "C":
                    iCat = (i, j)
                elif grid[i][j] == "F":
                    target = (i, j)
        dp = {}

        def solve(turn, pCat, pMouse):
            rCat, cCat = pCat
            rMouse, cMouse = pMouse
            if pMouse == target:
                return True
            if pCat == pMouse or pCat == target or turn > 80:
                return False
            key = (turn, pCat, pMouse)
            if key in dp:
                return dp[key]
            if turn % 2 == 0:
                for d in direct:
                    for j in range(1, mouseJump + 1):
                        rNext, cNext = rMouse + d[0] * j, cMouse + d[1] * j
                        if rNext < 0 or rNext >= m or cNext < 0 or cNext >= n or grid[rNext][cNext] == '#':
                            break
                        if solve(turn + 1, pCat, (rNext, cNext)):
                            return True
                return False
            else:
                for d in direct:
                    for j in range(1, catJump + 1):
                        rNext, cNext = rCat + d[0] * j, cCat + d[1] * j
                        if rNext < 0 or rNext >= m or cNext < 0 or cNext >= n or grid[rNext][cNext] == '#':
                            break
                        if not solve(turn + 1, (rNext, cNext), pMouse):
                            return False
                if not solve(turn + 1, pCat, pMouse):
                    return False
                return True

        return solve(0, iCat, iMouse)


s = Solution()
print(s.canMouseWin(["####F",
                     "#C...",
                     "M...."], 1, 2))
