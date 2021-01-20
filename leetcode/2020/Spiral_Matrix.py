class Solution:
    def spiralOrder(self, a):
        m, n = len(a), len(a[0])
        res = []
        d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        i, j, k = 0, 0, 0
        while len(res) < m * n:
            res.append(a[i][j])
            a[i][j] = 101
            iNext, jNext = i + d[k][0], j + d[k][1]
            if iNext < 0 or iNext == m or jNext < 0 or jNext == n or a[iNext][jNext] == 101:
                k = (k + 1) % 4
                i += d[k][0]
                j += d[k][1]
            else:
                i, j = iNext, jNext
        return res


s = Solution()
print(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
