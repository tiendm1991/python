class Solution:
    def longestArithSeqLength(self, a) -> int:
        n = len(a)
        dp = [{} for i in range(n)]
        res = 2
        for i in range(1, n):
            for j in range(i):
                x = a[i] - a[j]
                if x in dp[j]:
                    dp[i][x] = dp[j][x] + 1
                else:
                    dp[i][x] = 2
                res = max(res, dp[i][x])
        return res


s = Solution()
print(s.longestArithSeqLength([9, 4, 7, 2, 10]))
print(s.longestArithSeqLength([20, 1, 15, 3, 10, 5, 8]))
