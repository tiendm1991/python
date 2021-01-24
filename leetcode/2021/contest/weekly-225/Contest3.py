class Solution:
    def kthLargestValue(self, matrix, k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        a = [[0 for j in range(n + 1)] for i in range(m + 1)]
        v = []
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                a[i][j] = matrix[i - 1][j - 1] ^ a[i - 1][j] ^ a[i][j - 1] ^ a[i - 1][j - 1]
                v.append(a[i][j])
        res = sorted(v, reverse=True)
        return res[k - 1]


s = Solution()
print(s.kthLargestValue([[5, 2], [1, 6]], 4))
