from heapq import heappush
from heapq import heappop
import collections


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        if self.y - self.x != other.y - other.x:
            return self.y - self.x > other.y - other.x
        return self.x < other.x

    def __str__(self):
        return f'{self.x}-{self.y}'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Solution:
    # using max heap with point(y-x, x)
    def findMaxValueOfEquation1(self, points, k: int) -> int:
        _max = -(10 ** 9 + 7)
        q = []
        points = [Point(p[0], p[1]) for p in points]
        for p1 in points:
            while q:
                p2 = heappop(q)
                if p1.x - p2.x <= k:
                    _max = max(_max, p1.x + p1.y + p2.y - p2.x)
                    heappush(q, p2)
                    break
            heappush(q, p1)
        return _max

    # using max heap with point(y-x, x)
    def findMaxValueOfEquation2(self, points, k: int) -> int:
        _max = -(10 ** 9 + 7)
        q = []
        points = [(p[0] - p[1], p[0]) for p in points]  # (x1-y1, x1)
        for p1 in points:
            while q:
                p2 = heappop(q)
                if p1[1] - p2[1] <= k:
                    _max = max(_max, - p1[0] + 2 * p1[1] - p2[0])  # -(x1 - y1) + 2x1 - (x2 - y2)
                    heappush(q, p2)
                    break
            heappush(q, p1)
        return _max

    # using monotonic queue (deque)
    def findMaxValueOfEquation(self, points, k: int) -> int:
        _max = -(10 ** 9 + 7)
        q = collections.deque()
        for p in points:
            while q and p[0] - q[0][1] > k:
                q.popleft()
            if q:
                _max = max(_max, q[0][0] + p[0] + p[1])
            while q and q[-1][0] <= p[1] - p[0]:
                q.pop()
            q.append([p[1] - p[0], p[0]])
        return _max


s = Solution()
print(s.findMaxValueOfEquation([[-19, -12], [-13, -18], [-12, 18], [-11, -8], [-7, 12], [-5, 16]], 6))
print(s.findMaxValueOfEquation([[-17, 5], [-10, -8], [-5, -13], [-2, 7], [8, -14]], 4))
print(s.findMaxValueOfEquation([[1, 3], [2, 0], [5, 10], [6, -10]], 1))
