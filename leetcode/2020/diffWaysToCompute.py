import functools
from datetime import datetime, time
import math

from testcases.cebu import Util
from testcases.cebu.Util import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diffWaysToCompute(self, input: str):
        def cal(a, b, opt):
            if opt == '+':
                return a + b
            elif opt == '-':
                return a - b
            else:
                return a * b

        def backtrack(a, start, end):
            if start == end:
                return [a[start]]
            result = []
            for i in range(start, end + 1):
                if str(a[i]) in '+-*':
                    x = backtrack(a, start, i - 1)
                    y = backtrack(a, i + 1, end)
                    for x1 in x:
                        for y1 in y:
                            result.append(cal(x1, y1, a[i]))
            return result

        def dpProgram(a):
            num = [x for x in a if str(x) not in '+-*']
            opt = [x for x in a if str(x) in '+-*']
            n = len(num)
            dp = [[[] for j in range(n)] for i in range(n)]
            for i in range(n - 1, -1, -1):
                for j in range(i, n):
                    if i == j:
                        dp[i][j].append(num[i])
                        continue
                    for k in range(i, j):
                        for x in dp[i][k]:
                            for y in dp[k + 1][j]:
                                dp[i][j].append(cal(x, y, opt[k]))
            return dp[0][n - 1]

        pre, idx = 0, 0
        a = []
        while idx < len(input):
            if str(input[idx]) in '+-*':
                a.append(int(input[pre:idx]))
                a.append(input[idx])
                pre = idx + 1
            idx += 1
        a.append(int(input[pre:]))
        result = dpProgram(a)
        result.sort()
        return result


s = Solution()
startTime = datetime.now()
print(s.diffWaysToCompute("2-1-1"))
print(datetime.now() - startTime)
