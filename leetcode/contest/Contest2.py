class Solution:
    def numTeams(self, rating) -> int:
        n = len(rating)
        if n < 3:
            return 0
        dp = [[0 for i in range(2)] for j in range(n)]
        for i in range(1, n):
            for j in range(i):
                if rating[j] < rating[i]:
                    dp[i][0] += 1
                else:
                    dp[i][1] += 1
        count = 0
        for i in range(2, n):
            for j in range(1, i):
                if rating[j] < rating[i]:
                    count += dp[j][0]
                else:
                    count += dp[j][1]
        return count


s = Solution()
print(s.numTeams([1, 2, 3, 4]))
