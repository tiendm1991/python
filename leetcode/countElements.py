from datetime import datetime
import functools


class Solution:
    def countElements(self, arr) -> int:
        d = {}
        count = 0
        for x in arr:
            if x not in d:
                if x - 1 in d:
                    count += d[x - 1]
                d[x] = 1
            else:
                d[x] += 1
            if x + 1 in d:
                count += 1
        return count


s = Solution()
startTime = datetime.now()
print(s.matrixReshape([[1, 2], [3, 4]], 1, 4))
print(datetime.now() - startTime)
