class Solution:
    def getMaxGridHappiness1(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        memo = {}
        mask = [[0 for j in range(n)] for i in range(m)]

        def helper(x, inRemain, exRemain):
            if x == m * n or (inRemain == 0 and exRemain == 0):
                return 0
            # preState is previous row assigned
            # ex:
            # [0, 1, 2],
            # [2, 1, 0]
            # r, c = (1, 1) => previous = [[1, 0], [0, 2], [0, 1] = [2, 2, 1]
            preState = ""
            for pre in range(x - 1, x - 1 - n, -1):
                if pre >= 0:
                    iy, jy = pre // n, pre % n
                    preState += str(mask[iy][jy])
                else:
                    preState += "#"
            if (x, inRemain, exRemain, preState) in memo:
                return memo[(x, inRemain, exRemain, preState)]
            i, j = x // n, x % n
            res = helper(x + 1, inRemain, exRemain)
            if inRemain > 0:
                inScore = 120
                if i - 1 >= 0:
                    if mask[i - 1][j] == 1:
                        inScore += -30 - 30
                    elif mask[i - 1][j] == 2:
                        inScore += -30 + 20
                if j - 1 >= 0:
                    if mask[i][j - 1] == 1:
                        inScore += -30 - 30
                    elif mask[i][j - 1] == 2:
                        inScore += -30 + 20
                mask[i][j] = 1
                inScore += helper(x + 1, inRemain - 1, exRemain)
                res = max(res, inScore)
            if exRemain > 0:
                exScore = 40
                if i - 1 >= 0:
                    if mask[i - 1][j] == 1:
                        exScore += 20 - 30
                    elif mask[i - 1][j] == 2:
                        exScore += 20 + 20
                if j - 1 >= 0:
                    if mask[i][j - 1] == 1:
                        exScore += 20 - 30
                    elif mask[i][j - 1] == 2:
                        exScore += 20 + 20
                mask[i][j] = 2
                exScore += helper(x + 1, inRemain, exRemain - 1)
                res = max(res, exScore)
            mask[i][j] = 0
            memo[(x, inRemain, exRemain, preState)] = res
            return res

        return helper(0, introvertsCount, extrovertsCount)

    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        memo = {}
        mask = [[0 for j in range(n)] for i in range(m)]

        def helper(r, c, inRemain, exRemain):
            if r == m or (inRemain == 0 and exRemain == 0):
                return 0
            if c == n:
                return helper(r + 1, 0, inRemain, exRemain)
            # preState is previous row assigned
            # ex:
            # [0, 1, 2],
            # [2, 1, 0]
            # r, c = (1, 1) => previous = [[1, 0], [0, 2], [0, 1] = [2, 2, 1]
            preState = ""
            for i in range(c - 1, -1, -1):
                preState += str(mask[r][i])
            if r == 0:
                preState += "#" * (n - c)
            else:
                for i in range(n - 1, c - 1, -1):
                    preState += str(mask[r - 1][i])
            if (r, c, inRemain, exRemain, preState) in memo:
                return memo[(r, c, inRemain, exRemain, preState)]
            res = helper(r, c + 1, inRemain, exRemain)
            if inRemain > 0:
                inScore = 120
                if r - 1 >= 0:
                    if mask[r - 1][c] == 1:
                        inScore += -30 - 30
                    elif mask[r - 1][c] == 2:
                        inScore += -30 + 20
                if c - 1 >= 0:
                    if mask[r][c - 1] == 1:
                        inScore += -30 - 30
                    elif mask[r][c - 1] == 2:
                        inScore += -30 + 20
                mask[r][c] = 1
                inScore += helper(r, c + 1, inRemain - 1, exRemain)
                res = max(res, inScore)
            if exRemain > 0:
                exScore = 40
                if r - 1 >= 0:
                    if mask[r - 1][c] == 1:
                        exScore += 20 - 30
                    elif mask[r - 1][c] == 2:
                        exScore += 20 + 20
                if c - 1 >= 0:
                    if mask[r][c - 1] == 1:
                        exScore += 20 - 30
                    elif mask[r][c - 1] == 2:
                        exScore += 20 + 20
                mask[r][c] = 2
                exScore += helper(r, c + 1, inRemain, exRemain - 1)
                res = max(res, exScore)
            mask[r][c] = 0
            memo[(r, c, inRemain, exRemain, preState)] = res
            return res

        return helper(0, 0, introvertsCount, extrovertsCount)


s = Solution()
print(s.getMaxGridHappiness(2, 3, 1, 2), s.getMaxGridHappiness(2, 3, 1, 2))
print(s.getMaxGridHappiness(3, 1, 2, 1), s.getMaxGridHappiness(3, 1, 2, 1))
print(s.getMaxGridHappiness(3, 3, 3, 1), s.getMaxGridHappiness(3, 3, 3, 1))
