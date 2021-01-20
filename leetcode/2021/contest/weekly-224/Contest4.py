import functools


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

        @functools.lru_cache(None)
        def solve(turn, pCat, pMouse):
            rCat, cCat = pCat
            rMouse, cMouse = pMouse
            if pMouse == target:
                return True
            if pCat == target or pCat == pMouse or turn > 100:
                return False
            if turn % 2 == 0:
                for d in direct:
                    for j in range(1, mouseJump + 1):
                        rNext, cNext = rMouse + d[0] * j, cMouse + d[1] * j
                        if 0 <= rNext < m and 0 <= cNext < n and grid[rNext][cNext] != '#':
                            if solve(turn + 1, pCat, (rNext, cNext)):
                                return True
                        else:
                            break
                if solve(turn + 1, pCat, pMouse):
                    return True
                return False
            else:
                for d in direct:
                    for j in range(1, catJump + 1):
                        rNext, cNext = rCat + d[0] * j, cCat + d[1] * j
                        if 0 <= rNext < m and 0 <= cNext < n and grid[rNext][cNext] != '#':
                            if not solve(turn + 1, (rNext, cNext), pMouse):
                                return False
                        else:
                            break
                if not solve(turn + 1, pCat, pMouse):
                    return False
                return True

        return solve(0, iCat, iMouse)


s = Solution()
print(s.canMouseWin(["####.##",
                     ".#C#F#.",
                     "######.",
                     "##M.###"], 3, 6))
print(s.canMouseWin(["####F",
                     "#C...",
                     "M...."], 1, 2))
