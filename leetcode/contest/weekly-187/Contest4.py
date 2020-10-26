from datetime import datetime
from heapq import heappush
from heapq import heappop


class HeapElement:
    def __init__(self, idx: tuple, s):
        self.idx = idx
        self.s = s

    def __str__(self):
        return '{}-{}'.format(self.idx, self.s)

    def __cmp__(self, other):
        return self.s - other.s

    def __lt__(self, other):
        return self.s < other.s


class Solution:
    def kthSmallest(self, mat, k: int) -> int:
        m, n = len(mat), len(mat[0])
        count = 1
        initTupple = tuple(0 for i in range(m))
        initS = sum([mat[i][0] for i in range(m)])
        a = [HeapElement(initTupple, initS)]
        exist = {initTupple}
        while count < k:
            count += 1
            top = heappop(a)
            t = list(top.idx)
            s = top.s
            for i in range(m):
                if t[i] < n - 1:
                    t[i] += 1
                    newT = tuple(t)
                    if newT not in exist:
                        newS = s + mat[i][t[i]] - mat[i][t[i] - 1]
                        heappush(a, HeapElement(newT, newS))
                        exist.add(newT)
                    t[i] -= 1
        return heappop(a).s


s = Solution()
startTime = datetime.now()
print(s.kthSmallest([[1, 10, 10],
                     [1, 4, 5],
                     [2, 3, 6]], 7))
print(datetime.now() - startTime)
