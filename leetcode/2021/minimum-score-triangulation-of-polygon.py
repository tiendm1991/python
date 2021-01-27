class Solution:
    def minScoreTriangulation_topdown(self, a) -> int:
        n = len(a)
        dp = {}

        def helper(start, end):
            if end - start < 2:
                return 0
            key = (start, end)
            if key in dp:
                return dp[key]
            res = float("inf")
            for k in range(start + 1, end):
                res = min(res, a[start] * a[end] * a[k] + helper(start, k) + helper(k, end))
            dp[key] = res
            return res

        return helper(0, n - 1)

    def minScoreTriangulation(self, a) -> int:
        n = len(a)
        dp = [[float("inf") for j in range(n)] for i in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if j - i < 2:
                    dp[i][j] = 0
                    continue
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], a[i] * a[j] * a[k] + dp[i][k] + dp[k][j])
        return dp[0][n - 1]


s = Solution()
print(s.minScoreTriangulation([3, 7, 4, 5]))
print(s.minScoreTriangulation([1, 3, 1, 4, 1, 5]))
