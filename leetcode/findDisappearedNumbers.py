import functools
from datetime import datetime, time
import math
import bisect
import random
import collections

class Solution:
    def findDisappearedNumbers(self, nums):
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])
        return [i + 1 for i, num in enumerate(nums) if num > 0]
s = Solution()
startTime = datetime.now()
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(datetime.now() - startTime)

