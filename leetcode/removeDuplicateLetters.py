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
        for i in range(s):
            ch = s[i]
            if count[ch] == 1:
                stack.append(ch)
                continue
            

        return stack

s = Solution()
startTime = datetime.now()
print(s.removeDuplicateLetters('bcabc'))
print(datetime.now() - startTime)

