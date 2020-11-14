class Solution:
    def matrixScore(self, a) -> int:
        m, n = len(a), len(a[0])
        for i in range(m):
            if a[i][0] == 0:
                for j in range(n):
                    a[i][j] = 1 - a[i][j]
        for j in range(1, n):
            x = 0
            for i in range(m):
                x += a[i][j]
            if x < m - x:
                for i in range(m):
                    a[i][j] = 1 - a[i][j]
        ans = 0
        for i in range(m):
            for j in range(n):
                ans += a[i][j] * 1 << (n - 1 - j)
        return ans


s = Solution()
print(s.matrixScore([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]))
