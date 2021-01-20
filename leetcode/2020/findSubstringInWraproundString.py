import functools
from datetime import datetime, time
import math
import bisect
import random
import collections


class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        n = len(p)
        dp = [1] * n
        dict = {p[i]: 1 for i in range(n)}
        for i in range(1, n):
            diff = ord(p[i]) - ord(p[i - 1])
            if p[i] == 'a':
                diff += 26
            if diff == 1:
                dp[i] += dp[i - 1]
            dict[p[i]] = max(dict[p[i]], dp[i])
        return sum(dict.values())


s = Solution()
startTime = datetime.now()
print(s.findSubstringInWraproundString('bcabc'))
print(datetime.now() - startTime)
