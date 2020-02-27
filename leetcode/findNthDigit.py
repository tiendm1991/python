import functools
from datetime import datetime, time
import math


class Solution:
    def findNthDigit(self, n: int) -> int:
        x = 0
        nbDigit = 0
        while x < n:
            x += (nbDigit + 1) * (pow(10, nbDigit+1) - pow(10, nbDigit))
            nbDigit += 1
        if x == n:
            return 9
        n -= x - (nbDigit) * (pow(10, nbDigit) - pow(10, nbDigit-1))
        a = pow(10, nbDigit-1) + n//nbDigit - 1
        if n % nbDigit == 0:
            return a%10
        return int(str(a+1)[n%nbDigit-1])

s = Solution()
startTime = datetime.now()
print(s.findNthDigit(24))
print(datetime.now() - startTime)

