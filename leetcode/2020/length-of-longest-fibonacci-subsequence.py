class Solution:
    def lenLongestFibSubseq(self, a) -> int:
        dp = {}
        res = 0
        dp[0] = {}
        dp[1] = {a[0]: 2}
        for i in range(2, len(a)):
            dp[i] = {}
            for j in range(i):
                k = a[i] - a[j]
                dp[i][a[j]] = 2
                if k in dp[j]:
                    dp[i][a[j]] = max(dp[i][a[j]], dp[j][k] + 1)
                res = max(res, dp[i][a[j]])
        return res if res > 2 else 0


s = Solution()
print(s.lenLongestFibSubseq([1, 3, 7, 11, 12, 14, 18]))
print(s.lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8]))
