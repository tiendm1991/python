import functools
from datetime import datetime, time

import math


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def combinationSum3(self, k: int, n: int):
        result = []
        a = []

        def backtrack(result, a, k, n, s, start):
            if len(a) > k:
                return
            if len(a) == k:
                if s == n and a not in result:
                    result.append(a[::])
                return
            for i in range(start, 10):
                if s + i <= n:
                    a.append(i)
                    s += i
                    backtrack(result, a, k, n, s, i + 1)
                    del a[-1]
                    s -= i

        backtrack(result, a, k, n, 0, 1)
        return result


s = Solution()
startTime = datetime.now()
print(s.combinationSum3(3, 7))
print(datetime.now() - startTime)
