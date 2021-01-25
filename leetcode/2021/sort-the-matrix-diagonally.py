class Solution:
    def diagonalSort(self, mat):
        m, n = len(mat), len(mat[0])
        if m == 1 or n == 1:
            return mat

        def fill(x, y):
            a = []
            i, j = x, y
            while i < m and j < n:
                a.append(mat[i][j])
                i += 1
                j += 1
            a.sort()
            idx = 0
            while x + idx < m and y + idx < n:
                mat[x + idx][y + idx] = a[idx]
                idx += 1

        for i in range(1, m):
            fill(i, 0)
        for i in range(n):
            fill(0, i)
        return mat


s = Solution()
print(s.diagonalSort([[3, 3, 1, 1],
                      [2, 2, 1, 2],
                      [1, 1, 1, 2]]))
