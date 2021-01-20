from datetime import datetime, time
import heapq
import math
import random
import collections


class Solution:
    def findMinDifference(self, timePoints) -> int:
        n = len(timePoints)
        a = [0] * n
        for i in range(n):
            s = timePoints[i].split(':')
            a[i] = int(s[0]) * 60 + int(s[1])
        a.sort()
        _min = 1440
        for i in range(1, n):
            _min = min(_min, a[i] - a[i - 1])
        return min(_min, a[0] + 1440 - a[-1])


s = Solution()
startTime = datetime.now()
print(s.findMinDifference(["23:59", "00:00"]))
print(datetime.now() - startTime)
