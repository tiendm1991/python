from datetime import datetime


class Solution:
    def canJump(self, nums) -> bool:
        n = len(nums)
        dp = [False for i in range(n)]
        dp[0] = True
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if dp[j] and j + nums[j] >= i:
                    dp[i] = True
                    break
        return dp[n - 1]


s = Solution()
start = datetime.now()
print(s.canJump([1, 2, 3, 4]))
print(datetime.now() - start)
