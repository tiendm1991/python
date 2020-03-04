import functools
from datetime import datetime, time
import math
import bisect
import random


class Solution:
    def removeDuplicateLetters(self, s: str):
        stack = []
        n = len(s)
        i = n-1
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        for ch in s:
            if ch not in stack:
                while len(stack) > 0 and stack[-1] > ch and count[stack[-1]] > 0:
                    stack.pop()
                stack.append(ch)
            count[ch] -= 1
        return ''.join(stack)

    def removeDuplicateLetters2(self, s: str):
        stack = []
        n = len(s)
        i = n-1
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        for ch in s:
            if ch not in stack:
                stack.append(ch)
            else:
                idx = stack.index(ch)
                replace = False
                idx2 = idx
                for j in range(idx + 1, len(stack)):
                    if stack[j] < ch:
                        idx2 = j
                        replace = True
                        break
                for k in range(idx + 1, idx2):
                    if count[stack[k]] <= 0:
                        replace = False
                        break
                if replace:
                    del stack[idx]
                    stack.append(ch)
            count[ch] -= 1
        return ''.join(stack)

s = Solution()
startTime = datetime.now()
print(s.removeDuplicateLetters('bcabc'))
print(datetime.now() - startTime)

