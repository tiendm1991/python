from datetime import datetime
import functools


class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        mod = 10 ** 9 + 7
        if m == 0 or n == 0 or N == 0:
            return 0
        if m == 0 and n == 0:
            if N == 1:
                return 4
            else:
                return 0
        dp = [[[-1 for k in range(N + 1)] for j in range(n)] for i in range(m)]

        def dfs(r, c, step):
            if step <= 0:
                return 0
            s = 0
            if step == 1:
                if r == 0:
                    s += 1
                if r == m - 1:
                    s += 1
                if c == 0:
                    s += 1
                if c == n - 1:
                    s += 1
                return s
            if dp[r][c][step] != -1:
                return dp[r][c][step]
            if r - 1 >= 0:
                s += dfs(r - 1, c, step - 1)
            if c - 1 >= 0:
                s += dfs(r, c - 1, step - 1)
            if r + 1 < m:
                s += dfs(r + 1, c, step - 1)
            if c + 1 < n:
                s += dfs(r, c + 1, step - 1)
            s %= mod
            dp[r][c][step] = s
            return s

        result = 0
        for step in range(1, N + 1):
            result = (result + dfs(i, j, step)) % mod
        return result % mod


s = Solution()
startTime = datetime.now()
print(s.findPaths(1, 3, 3, 0, 1))
print(datetime.now() - startTime)
