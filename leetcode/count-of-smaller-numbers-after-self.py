import functools
from datetime import datetime, time
import math

from testcases.cebu import Util
from testcases.cebu.Util import *
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
        root = TreeNode(nums[0])
        for i in range(1, n):
            x = nums[i]
            cur = root
            while True:
                if cur.val > x:
                    cur.child += 1
                    if cur.left == None:
                        cur.left = TreeNode(x)
                        break
                    else:
                        cur = cur.left
                        continue
                else:
                    if cur.right == None:
                        cur.right = TreeNode(x)
                        break
                    else:
                        cur = cur.right
                        continue
        dp = [0] * n
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if nums[i] > nums[j]:
                    dp[i] += 1
        return dp


s = Solution()
startTime = datetime.now()
print(s.countSmaller([2,0,1]))
print(datetime.now() - startTime)

