class Solution:
    def ways(self, pizza, k: int) -> int:
        if k == 1:
            return 1
        mod = 10 ** 9 + 7
        m, n = len(pizza), len(pizza[0])
        a = [[1 if p[i] == 'A' else 0 for i in range(n)] for p in pizza]
        x = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                x[i][j] = a[i - 1][j - 1] + x[i][j - 1] + x[i - 1][j] - x[i - 1][j - 1]
        dp = [[[-1 if x != 1 else 0 for x in range(k + 1)] for y in range(n + 1)] for z in range(m + 1)]

        def caculate(r1, c1, r2, c2):
            return x[r2][c2] - x[r1 - 1][c2] - x[r2][c1 - 1] + x[r1 - 1][c1 - 1]

        def recursive(r, c, k):
            if r > m or c > n or m + n - r - c < k - 1:
                return 0
            if k == 1 and caculate(r, c, m, n) > 0:
                return 1
            if dp[r][c][k] != -1:
                return dp[r][c][k]
            count = 0
            for i in range(r, m):
                if caculate(r, c, i, n) > 0:
                    count += recursive(i + 1, c, k - 1)  # cut horizontally
            for i in range(c, n):
                if caculate(r, c, m, i) > 0:
                    count += recursive(r, i + 1, k - 1)  # cut vertically
            count %= mod
            dp[r][c][k] = count
            return count

        return recursive(1, 1, k)


s = Solution()
print(s.ways(["A..", "AA.", "..."], 3))
