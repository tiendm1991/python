from datetime import datetime, time


class Solution:
    def predictTheWinner(self, nums) -> bool:
        n = len(nums)
        if n < 3:
            return True
        dp = [[0 for j in range(n)] for i in range(n)]
        for i in range(n-1, -1, -1):
            s = 0
            for j in range(i, n):
                s += nums[j]
                if i == j:
                    dp[i][j] = s
                    continue
                dp[i][j] = s - min(dp[i+1][j], dp[i][j-1])
                # dp[i][j] = max(s - dp[i+1][j], s - dp[i][j-1])
        return dp[0][n-1] > sum(nums) - dp[0][n-1]

s = Solution()
startTime = datetime.now()
print(s.predictTheWinner([1,4,2,5,3,6]))
print(datetime.now() - startTime)

