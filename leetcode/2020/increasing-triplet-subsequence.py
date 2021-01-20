import functools
from datetime import datetime, time
import math


class Solution:
    def increasingTriplet1(self, nums) -> bool:
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

    def increasingTriplet_short(self, nums) -> bool:
        n = len(nums)
        _min = nums[0]
        first, second = float('inf'), float('inf')
        for i in range(n):
            if nums[i] <= first:
                first = nums[i]
            elif nums[i] <= second:
                second = nums[i]
            else:
                return True
        return False

    def increasingTriplet(self, nums) -> bool:
        n = len(nums)
        _min = nums[0]
        hasLess = [False] * n
        for i in range(1, n):
            if nums[i] > _min:
                hasLess[i] = True
            elif nums[i] < _min:
                _min = nums[i]
        _max = nums[-1]
        for i in range(n - 2, 0, -1):
            if nums[i] < _max and hasLess[i]:
                return True
            elif nums[i] > _max:
                _max = nums[i]
        return False


s = Solution()
startTime = datetime.now()
print(s.increasingTriplet([1, 2, 3, 1, 2, 1]))
print(s.increasingTriplet([1, 2, 1, 2, 1, 2, 1, 2, 1, 2]))
print(datetime.now() - startTime)
