import functools
from datetime import datetime, time
import math


class Solution:
    def countDigitOne(self, num: int) -> int:
        if num < 1:
            return 0

        def countByNbdigit(nbDigit):
            if nbDigit <= 1:
                return nbDigit
            return 10 * countByNbdigit(nbDigit - 1) + pow(10, nbDigit - 1)

        def cal(firstDigit, nbTailZero):
            if firstDigit == 0:
                return 0
            if nbTailZero == 0:
                return 1 if firstDigit > 0 else 0
            if firstDigit == 1:
                return 1 + countByNbdigit(nbTailZero)
            else:
                return firstDigit * countByNbdigit(nbTailZero) + pow(10, nbTailZero)

        s = str(num)
        n = len(s)
        if n == 1:
            return 1
        count = 0
        for i in range(n):
            if s[i] != '1':
                count += cal(int(s[i]), n - 1 - i)
            elif i < n - 1:
                count += int(s[i + 1:]) + cal(int(s[i]), n - 1 - i)
            else:
                count += 1
        return count


s = Solution()
startTime = datetime.now()
print(s.countDigitOne(100))
print(datetime.now() - startTime)
