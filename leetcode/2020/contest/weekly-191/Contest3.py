from builtins import list
from itertools import count
from typing import re

from leetcode import Util
from leetcode.Util import TreeNode


class Solution:
    def minReorder(self, n: int, connections) -> int:
        d = {i: set() for i in range(n)}
        d2 = {i: set() for i in range(n)}
        for c in connections:
            d[c[0]].add(c[1])
            d2[c[1]].add(c[0])

        def dfs(vList):
            if len(vList) == 0:
                return 0
            reorder = 0
            lsNeighbor = set()
            for v in vList:
                lsNeighbor |= d2[v]
                for i in d2[v]:
                    d[i].remove(v)
                reorder += len(d[v])
                for i in d[v]:
                    d2[i].remove(v)
                lsNeighbor |= d[v]
            reorder += dfs(lsNeighbor)
            return reorder

        return dfs({0})


s = Solution()
print(s.minReorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]))
