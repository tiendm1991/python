class Solution:
    def threeSumMulti1(self, a, target: int) -> int:
        mod = 10 ** 9 + 7
        n = len(a)
        d = [{} for i in range(n)]
        for i in range(1, n - 1):
            x = a[i]
            for j in range(i):
                d[i][x + a[j]] = d[i].get(x + a[j], 0) + 1
        res = 0
        for i in range(2, n):
            for j in range(1, i):
                res = (res + d[j].get(target - a[i], 0)) % mod
        return res

    def threeSumMulti(self, a, target: int) -> int:
        mod = 10 ** 9 + 7
        n = len(a)
        dp = [[[1 if k == 0 and j == 0 else 0 for k in range(4)] for j in range(target + 1)] for i in
              range(n + 1)]
        for i in range(1, n + 1):
            x = a[i - 1]
            for j in range(target + 1):
                for k in range(1, 4):
                    dp[i][j][k] = dp[i - 1][j][k]
                    if j >= x:
                        dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j - x][k - 1]) % mod
        return dp[n][target][3]


s = Solution()
print(s.threeSumMulti([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8))
