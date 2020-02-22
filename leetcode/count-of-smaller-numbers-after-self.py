import functools
from datetime import datetime, time
import math

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.child = 0
        self.visited = False

class Solution:
    def countSmaller(self, nums):
        n = len(nums)
        if n == 0:
            return []
        if n == 1:
            return [0]

        dp = [0] * n
        for i in range(n):
            x = nums[i]
            dp[i] = cur.child
            cur.visited = True
        return dp


s = Solution()
startTime = datetime.now()
print(s.countSmaller([5,2,6,2,1]))
print(datetime.now() - startTime)

