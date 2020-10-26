import functools
from datetime import datetime, time
import math
import bisect
import random


class Solution:
    def countSmaller(self, nums):
        n = len(nums)
        if n == 0:
            return []

        def floorSearch(arr, x, l, h):
            if arr[h] <= x:
                return arr[h]
            if l == h:
                return None
            m = (l + h + 1) // 2
            if arr[m] == x:
                return x
            elif arr[m] < x:
                return floorSearch(arr, x, m, h)
            elif m > l:
                return floorSearch(arr, x, l, m - 1)
            return None

        dp = [0] * n
        count = {nums[-1]: 1}
        lastIdx = {nums[-1]: n - 1}
        exist = [nums[-1]]
        for i in range(n - 2, -1, -1):
            x = floorSearch(exist, nums[i] - 1, 0, len(exist) - 1)
            if x != None:
                dp[i] += count[x]
                dp[i] += dp[lastIdx[x]]
                for j in range(i + 1, lastIdx[x]):
                    if nums[j] < nums[i]:
                        dp[i] += 1
            count[nums[i]] = count.get(nums[i], 0) + 1
            bisect.insort(exist, nums[i])
            lastIdx[nums[i]] = i
        return dp


s = Solution()
startTime = datetime.now()
print(s.countSmaller([4, 5, 3, 2, 2, 4, 1, 2, 3]))
print(datetime.now() - startTime)
