import functools
from datetime import datetime, time
import math
import bisect
import random
import collections

from testcases.cebu import Util
from testcases.cebu.Util import TreeNode


class Solution:
    def numTimesAllBlue(self, light) -> int:
        _max, l = 0, 0
        count = 0
        for x in light:
            _max = max(_max, x)
            l += 1
            if _max == l:
                count += 1
        return count

s = Solution()
startTime = datetime.now()
print(s.numTimesAllBlue([2,1,3,5,4]))
print(datetime.now() - startTime)

