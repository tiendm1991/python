import functools
from datetime import datetime, time
import math


class Solution:
    def minPatches(self, nums, n: int) -> int:
        m = len(nums)
        dp = [[False for j in range(n+1)] for j in range(m+1)]
        dp[0][0] = True
        for i in range(1, m+1):
            x = nums[i-1]
            for j in range(n+1):
                dp[i][j] = dp[i-1][j] or dp[i-1][j - x]
        while True:
            arr = dp[-1]
            added = False
            for i in range(len(arr)):
                if not arr[i]:
                    nums.append(i)
                    added = True
                    break
            if not added:
                break
            dp.append(dp[-1][::])
            x = nums[-1]
            i = len(dp) - 1
            for j in range(n+1):
                dp[i][j] = dp[i][j] or dp[i-1][j - x]
        return len(nums) - m
s = Solution()
startTime = datetime.now()
print(s.minPatches([1,2,2], 0))
print(datetime.now() - startTime)

