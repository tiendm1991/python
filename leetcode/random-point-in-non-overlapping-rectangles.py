from datetime import datetime, time
import heapq
import math

import random


class Solution:

    def __init__(self, rects):
        self.rects = rects
        self.weight = [0] * len(rects)
        for i in range(len(rects)):
            [x1, y1, x2, y2] = rects[i]
            w = (x2 - x1 + 1) * (y2 - y1 + 1)
            self.weight[i] = self.weight[i - 1] + w if i > 0 else w

    def pick(self) -> 'List[int]':
        area = random.randrange(0, self.weight[-1] + 1)

        def findCeil(s, f):
            if s == f or self.weight[s] >= area:
                return s
            mid = (s + f) // 2
            if self.weight[mid] < area:
                return findCeil(mid + 1, f)
            else:
                return findCeil(s, mid)

        [x1, y1, x2, y2] = self.rects[findCeil(0, len(self.rects) - 1)]
        x = random.randrange(x1, x2 + 1)
        y = random.randrange(y1, y2 + 1)
        return [x, y]


s = Solution([[82918473, -57180867, 82918476, -57180863],
              [83793579, 18088559, 83793580, 18088560],
              [66574245, 26243152, 66574246, 26243153],
              [72983930, 11921716, 72983934, 11921720]])
startTime = datetime.now()
print(s.pick())
print(datetime.now() - startTime)
