from datetime import datetime
import math

class Solution:
    def destCity(self, paths) -> str:
        d = {p[0] for p in paths}
        for p in paths:
            if p[1] not in d:
                return p[1]
        return None

s = Solution()
startTime = datetime.now()
print(s.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
print(datetime.now() - startTime)