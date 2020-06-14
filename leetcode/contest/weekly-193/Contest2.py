import collections
from heapq import heappush
from heapq import heappop

class Num:
    def __init__(self, val, count):
        self.val = val
        self.count = count
    def __lt__(self, other):
        return self.count < other.count

class Solution:
    def findLeastNumOfUniqueInts(self, arr, k: int) -> int:
        d = collections.Counter(arr)
        q = []
        for x in d:
            heappush(q, Num(x, d[x]))
        while k > 0:
            pop = heappop(q)
            if pop.count > k:
                pop.count -= k
                heappush(q, pop)
                break
            else:
                k -= pop.count
        return len(q)

s = Solution()
print(s.findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 3))
