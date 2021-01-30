class Solution:
    def numSubmatrixSumTarget(self, matrix, target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        res = 0
        for i in range(m):
            a = [0] * n
            for j in range(i, m):
                for k in range(n):
                    a[k] += matrix[j][k]
                d = {0: 1}
                s = 0
                for k in range(n):
                    s += a[k]
                    res += d.get(s - target, 0)
                    d[s] = d.get(s, 0) + 1
        return res


s = Solution()
print(s.numSubmatrixSumTarget([[1, -1],
                               [-1, 1]], 0))
print(s.numSubmatrixSumTarget([[0, 1, 0],
                               [1, 1, 1],
                               [0, 1, 0]], 0))
