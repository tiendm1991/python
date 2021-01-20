from datetime import datetime, time
import heapq
import math
import random
import collections


class Solution:
    count = 0

    def countArrangement(self, N: int) -> int:
        def backtrack(selected, idx):
            if idx == N:
                self.count += 1
                return
            for x in range(1, N + 1):
                poisition = idx + 1
                if not selected[x - 1]:
                    if (x >= poisition and x % poisition == 0) or (x <= poisition and poisition % x == 0):
                        selected[x - 1] = True
                        backtrack(selected, poisition)
                        selected[x - 1] = False

        selected = [False] * N
        backtrack(selected, 0)
        return self.count


s = Solution()
startTime = datetime.now()
print(s.countArrangement(2))
print(datetime.now() - startTime)
