import collections
from datetime import datetime


class Solution:
    def findDiagonalOrder(self, nums):
        n = len(nums)
        d = {}
        for i, r in enumerate(nums):
            for j, v in enumerate(r):
                k = i + j
                if k not in d:
                    d[k] = [v]
                else:
                    d[k].append(v)
        result = []
        for k in d:
            result += d[k][::-1]
        return result
s = Solution()
start = datetime.now()
print(s.findDiagonalOrder([[1,2,3],[4],[5,6,7],[8],[9,10,11]]))
print(datetime.now() - start)
