import functools
from datetime import datetime, time
import math
import bisect
import random
import collections


class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        s3 = -9999999
        for n in nums[::-1]:
            if n < s3:
                return True
            while stack and stack[-1] < n:
                s3 = stack.pop()
            stack.append(n)
        return False


s = Solution()
startTime = datetime.now()
print(s.find132pattern([8, 10, 2, 3, 2, 4, 6]))
print(datetime.now() - startTime)
