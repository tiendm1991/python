import functools
from datetime import datetime, time
import math


class Solution:
    def nthSuperUglyNumber(self, n: int, primes) -> int:
        if n == 0:
            return 1
        ugly = [0] * n
        ugly[0] = 1
        m = len(primes)
        counter = [0] * m
        uglyCurrent = [x for x in primes]
        for i in range(1, n):
            next = min(uglyCurrent)
            ugly[i] = next
            for j in range(m):
                if uglyCurrent[j] == next:
                    counter[j] += 1
                    uglyCurrent[j] = ugly[counter[j]] * primes[j]
        return ugly[n - 1]


s = Solution()
startTime = datetime.now()
print(s.nthSuperUglyNumber(12, [2, 7, 13, 19]))
print(datetime.now() - startTime)
