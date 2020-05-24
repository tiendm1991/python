from datetime import datetime
import math


class Solution:
    def buildArray(self, target, n: int):
        idx = 0
        result = []
        for x in range(1, n+1):
            if idx == len(target):
                break
            result.append("Push")
            if x < target[idx]:
                result.append("Pop")
            elif x == target[idx]:
                idx += 1
        return result

s = Solution()
startTime = datetime.now()
print(s.buildArray([2,3,4], 4))
print(datetime.now() - startTime)