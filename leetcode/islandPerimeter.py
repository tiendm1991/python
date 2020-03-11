import functools
from datetime import datetime, time
import math
import bisect
import random
import collections


class Solution:
    def islandPerimeter(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        S = sum([x.count(1) for x in grid])
        s = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i - 1 >= 0 and grid[i-1][j] == 1:
                        s += 1
                    if j - 1 >= 0 and grid[i][j-1] == 1:
                        s += 1
        return S * 4 - s * 2


s = Solution()
startTime = datetime.now()
print(s.islandPerimeter([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]))
print(datetime.now() - startTime)

