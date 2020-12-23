class Solution:
    def cherryPickup_topdown(self, a) -> int:
        m, n = len(a), len(a[0])
        dp = {}

        def helper(r, c1, c2):
            if r == m or c1 < 0 or c1 == n or c2 < 0 or c2 == n:
                return 0
            if (r, c1, c2) in dp:
                return dp[(r, c1, c2)]
            res = a[r][c1] if c1 == c2 else a[r][c1] + a[r][c2]
            maxCherry = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    maxCherry = max(maxCherry, helper(r + 1, c1 + i, c2 + j))
            res += maxCherry
            dp[(r, c1, c2)] = res
            return res

        return helper(0, 0, n - 1)

    def cherryPickup(self, a) -> int:
        m, n = len(a), len(a[0])
        dp = [[[0 for k in range(n + 2)] for j in range(n + 2)] for i in range(m + 1)]
        for r in range(m - 1, -1, -1):
            for c1 in range(1, n + 1):
                for c2 in range(1, n + 1):
                    dp[r][c1][c2] = a[r][c1 - 1]
                    if c1 != c2:
                        dp[r][c1][c2] += a[r][c2 - 1]
                    preMax = 0
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            preMax = max(preMax, dp[r + 1][c1 + i][c2 + j])
                    dp[r][c1][c2] += preMax
        return dp[0][1][n]


s = Solution()
print(s.cherryPickup([[4, 1, 5, 7, 1],
                      [6, 0, 4, 6, 4],
                      [0, 9, 6, 3, 5]]))
print(s.cherryPickup([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]))
print(s.cherryPickup([[1, 0, 0, 3], [0, 0, 0, 3], [0, 0, 3, 3], [9, 0, 3, 3]]))
print(s.cherryPickup([[1, 0, 0, 0, 0, 0, 1], [2, 0, 0, 0, 0, 3, 0], [2, 0, 9, 0, 0, 0, 0], [0, 3, 0, 5, 4, 0, 0],
                      [1, 0, 2, 3, 0, 0, 6]]))
