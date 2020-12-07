class Solution:
    def generateMatrix(self, n: int):
        res = [[0 for j in range(n)] for i in range(n)]
        d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        x, i, j, k = 1, 0, 0, 0
        while x <= n * n:
            res[i][j] = x
            iNext, jNext = i + d[k][0], j + d[k][1]
            if iNext < 0 or iNext == n or jNext < 0 or jNext == n or res[iNext][jNext] != 0:
                k = (k + 1) % 4
                i += d[k][0]
                j += d[k][1]
            else:
                i, j = iNext, jNext
            x += 1
        return res


s = Solution()
print(s.generateMatrix(3))
print(s.generateMatrix(4))
