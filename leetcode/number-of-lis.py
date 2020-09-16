class Solution:
    def findNumberOfLIS(self, nums) -> int:
        if len(nums) < 2:
            return len(nums)
        n = len(nums)
        dp = [[1, 1] for i in range(n)]
        _max = 1
        for i in range(1, n):
            for j in range(i):
                if nums[i] <= nums[j]:
                    continue
                if dp[j][0] + 1 > dp[i][0]:
                    dp[i][0] = dp[j][0] + 1
                    dp[i][1] = dp[j][1]
                elif dp[j][0] + 1 == dp[i][0]:
                    dp[i][1] += dp[j][1]
            _max = max(dp[i][0], _max)
        ans = 0
        for i in range(n):
            ans += dp[i][1] * (dp[i][0] // _max)
        return ans


s = Solution()
print(s.findNumberOfLIS([1, 3, 5, 4, 7]))
