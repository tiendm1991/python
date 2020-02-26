import functools
from datetime import datetime, time
import math


class Solution:
    def increasingTriplet(self, nums) -> bool:
        n = len(nums)
        f, s = nums[0], None
        fTmp = f
        for i in range(1, n):
            if s == None:
                if nums[i] > f:
                    s = nums[i]
                else:
                    f = min(f, nums[i])
            else:
                if nums[i] > s:
                    return True
                elif nums[i] > f:
                    s = nums[i]
                elif nums[i] <= fTmp:
                    fTmp = nums[i]
                else:
                    f = fTmp
                    s = nums[i]
        return False
s = Solution()
startTime = datetime.now()
print(s.increasingTriplet([1,2,1,2,1,2,1,2,1,2]))
print(datetime.now() - startTime)

