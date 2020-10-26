import functools
from datetime import datetime, time

from testcases.cebu import Util
from testcases.cebu.Util import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        a, n = 0, len(nums)
        if n == 0:
            return 0
        start = 0
        _min = n
        _minGlobal = _min
        while start < n:
            a += nums[start]
            if a >= s:
                break
            start += 1
        if start == n:
            return 0
        _min = start
        a -= nums[start]
        j = 0
        for i in range(start, n):
            x = nums[i]
            a += x
            _min += 1
            while a - nums[j] >= s:
                a -= nums[j]
                _min -= 1
                j += 1
            _minGlobal = min(_minGlobal, _min)
        return _minGlobal


s = Solution()
startTime = datetime.now()
print(s.minSubArrayLen(
    15,
    [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]))
print(datetime.now() - startTime)
