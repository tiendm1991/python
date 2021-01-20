class Solution:
    def bestTeamScore(self, scores, ages) -> int:
        n = len(scores)
        a = [[ages[i], scores[i]] for i in range(n)]
        a.sort()
        dp = [a[i][1] for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                if a[i][0] == a[j][0]:
                    dp[i] = max(dp[i], dp[j] + a[i][1])
                elif a[i][1] >= a[j][1]:
                    dp[i] = max(dp[i], dp[j] + a[i][1])
        return max(dp)


s = Solution()
print(s.bestTeamScore([3, 2, 4, 7, 10, 1, 3],
                      [1, 1, 2, 2, 4, 4, 5]))
print(s.bestTeamScore([5, 5, 4, 6], [1, 1, 2, 2]))
print(s.bestTeamScore([5, 1, 2, 3], [1, 8, 9, 10]))
