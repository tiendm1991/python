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

s = Solution()
startTime = datetime.now()
print(s.removeDuplicateLetters('bcabc'))
print(datetime.now() - startTime)

