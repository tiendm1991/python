import collections


class Solution:
    def deleteAndEarn(self, nums) -> int:
        if len(nums) == 0:
            return 0
        d = collections.Counter(nums)
        n = max(d)
        if n < 2:
            return d[1]
        dp = [0] * (n + 1)
        dp[1] = d.get(1, 0)
        for i in range(2, n + 1):
            dp[i] = dp[i - 1]
            if i in d:
                dp[i] = max(dp[i], dp[i - 2] + i * d[i])
        return dp[n]


s = Solution()
print(s.deleteAndEarn([3, 1]))
