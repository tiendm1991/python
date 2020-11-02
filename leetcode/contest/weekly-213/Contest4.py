class Solution:
    def kthSmallestPath(self, destination, k: int) -> str:
        m, n = destination
        comb = [[1 if i == 0 else 0 for i in range(m + n + 1)] for j in range(m + n + 1)]
        for i in range(1, m + n + 1):
            for j in range(1, i + 1):
                comb[i][j] = comb[i - 1][j] + comb[i - 1][j - 1]
        ans = ''
        x, y = 0, 0
        while x < m or y < n:
            if x == m:
                ans += 'H'
                y += 1
                continue
            if y == n:
                ans += 'V'
                x += 1
                continue
            hWay = comb[m - x + n - y - 1][m - x]
            if k <= hWay:
                ans += 'H'
                y += 1
            else:
                k -= hWay
                ans += 'V'
                x += 1
        return ans


s = Solution()
print(s.kthSmallestPath([2, 3], 3))
