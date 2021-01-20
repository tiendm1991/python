class Solution:
    def largestSubmatrix(self, matrix) -> int:
        m, n = len(matrix), len(matrix[0])
        h = [[0 for j in range(n)] for i in range(m)]
        h[0] = matrix[0]
        res = 0
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] != 0:
                    h[i][j] = h[i - 1][j] + matrix[i][j]
        for r in h:
            r = sorted(r, reverse=True)
            for j in range(n):
                res = max(res, (j+1) * r[j])
        return res


s = Solution()
print(s.largestSubmatrix([[0, 0, 1], [1, 1, 1], [1, 0, 1]]))
