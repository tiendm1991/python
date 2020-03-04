import functools
from datetime import datetime, time
import math
import bisect
import random


class Solution:
    def maxSumSubmatrix(self, matrix, k: int) -> int:
        _max = -2147483648
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])

        def ceilSearch(arr, x, l, h):
            if x == 0:
                return 0
            if arr[l] >= x:
                return arr[l]
            if l == h:
                return None
            m = (l + h) // 2
            if arr[m] == x:
                return x
            elif arr[m] < x:
                if m < h:
                    return ceilSearch(arr, x, m + 1, h)
                else:
                    return None
            else:
                return ceilSearch(arr, x, l, m)

        def getMax(arr):
            n = len(arr)
            _set = [0]
            s = 0
            maxLocal = -2147483648
            for i in range(n):
                s += arr[i]
                x = ceilSearch(_set, s - k, 0, len(_set) - 1)
                if x != None:
                    maxLocal = max(maxLocal, s - x)
                if maxLocal == k:
                    return k
                bisect.insort(_set, s)
            return maxLocal

        for i in range(m):
            tmp = [0] * n
            for j in range(i, m):
                for a in range(n):
                    tmp[a] += matrix[j][a]
                x = getMax(tmp)
                if x == k:
                    return k
                _max = max(_max, x)
        return _max


s = Solution()
startTime = datetime.now()
print(s.maxSumSubmatrix([[5,-4,-3,4],
                         [-3,-4,4,5],
                         [5,1,5,-4]],10))
print(datetime.now() - startTime)

