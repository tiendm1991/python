class Solution:
    def longestSequence(self, a):
        n = len(a)
        dp = [{} for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                x = a[i] - a[j]
                if x in dp[j]:
                    dp[i][x] = dp[j][x] + 1
                else:
                    dp[i][x] = 2
        return max([max([x[1] for x in d.items()]) for d in dp if len(d) > 0])


s = Solution()
print(s.longestSequence([1, -2, 7, 3, -7, 4, 9, 2, -8, -5, -5, -7, 6, 2, -8, -9, 2, 5, 4, -10]))
