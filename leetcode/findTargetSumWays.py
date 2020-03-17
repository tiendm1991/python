from datetime import datetime, time


class Solution:
    def findTargetSumWays(self, nums, S: int) -> int:
        n = len(nums)
        dp = [{} for i in range(n)]
        if nums[0] == 0:
            dp[0][0] = 2
        else:
            dp[0][nums[0]] = 1
            dp[0][-nums[0]] = 1
        for i in range(1, n):
            x = nums[i]
            for k in dp[i-1]:
                dp[i][k+x] = dp[i].get(k+x, 0) + dp[i-1][k]
                dp[i][k-x] = dp[i].get(k-x, 0) + dp[i-1][k]
        if S not in dp[n-1]:
            return 0
        return dp[n-1][S]
s = Solution()
startTime = datetime.now()
print(s.findTargetSumWays([0,0,0,0,0,0,0,0,1], 1))
print(datetime.now() - startTime)

