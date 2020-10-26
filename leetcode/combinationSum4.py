import functools
from datetime import datetime, time
import math


class Solution:
    def combinationSum4(self, nums, target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        nums.sort()
        for i in range(1, target + 1):
            for x in nums:
                if i < x:
                    break
                dp[i] += dp[i - x]
        return dp[target]


s = Solution()
startTime = datetime.now()
print(s.combinationSum4([1, 2, 3], 5))
print(datetime.now() - startTime)
