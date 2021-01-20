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
    def calculate(self, s: str) -> int:
        s = s.strip()
        a = ['(']
        idx, num = 0, -1
        opts = '+-*/()'
        while idx < len(s):
            if s[idx] == ' ':
                idx += 1
                num = -1
                continue
            if s[idx] in opts:
                a.append(s[idx])
                num = -1
            else:
                if num == -1:
                    num = int(s[idx])
                else:
                    num = num * 10 + int(s[idx])
                if idx + 1 == len(s) or s[idx + 1] in opts or s[idx + 1] == ' ':
                    a.append(num)
            idx += 1
        a.append(')')
        i, n = 0, len(a)
        stack = []
        while i < n:
            if a[i] != ')':
                stack.append(a[i])
            else:
                cal = []
                while True:
                    y = stack.pop()
                    opt = stack.pop()
                    if opt == '(':
                        cal.append(y)
                        stack.append(sum(cal))
                        break
                    elif opt == '+':
                        cal.append(y)
                    else:
                        cal.append(-y)
            i += 1
        return stack.pop()


s = Solution()
startTime = datetime.now()
print(s.calculate("(1+(4+5+2)-3)+(6+8)"))
print(datetime.now() - startTime)
