from datetime import datetime, time
import heapq
import math
import random
import collections


class Solution:
    def findMaxLength2(self, nums) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + nums[i - 1]
        _max = 0
        for i in range(2, n + 1):
            for j in range(i - 1):
                if i - j == 2 * (dp[i] - dp[j]):
                    _max = max(_max, i - j)
        return _max

    def findMaxLength(self, nums) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1 if nums[i - 1] == 1 else dp[i - 1] - 1
        dict = {dp[0]: 0, dp[1]: 1}
        _max = 0
        for i in range(2, n + 1):
            if dp[i] in dict:
                _max = max(_max, i - dict[dp[i]])
            else:
                dict[dp[i]] = i
        return _max


s = Solution()
startTime = datetime.now()
print(s.findMaxLength([1, 1, 0, 1, 1, 0, 1, 1]))
print(datetime.now() - startTime)
