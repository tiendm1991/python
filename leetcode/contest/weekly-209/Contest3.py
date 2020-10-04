import math
from builtins import range


class Solution:
    def visiblePoints(self, points, angle: int, location) -> int:
        L = points.count(location)
        p = [x for x in points if x != location]
        n = len(p)
        if n == 1:
            return 1
        a, b = [], []
        for x, y in p:
            ang = math.atan2(y - location[1], x - location[0])
            a.append((ang + 2 * math.pi) % (2 * math.pi))  # inverse clockside
            b.append((180 - ang + 2 * math.pi) % (2 * math.pi))  # clockside

        eps = 10 ** -9
        ans = 0
        angle = angle * math.pi / 180

        a.sort()
        i = 0
        for j in range(1, n):
            while i < j and a[j] - a[i] - angle > eps:
                i += 1
            ans = max(ans, j - i + 1)

        b.sort()
        i = 0
        for j in range(1, n):
            while i < j and b[j] - b[i] - angle > eps:
                i += 1
            ans = max(ans, j - i + 1)
        return ans + L


s = Solution()
print(s.visiblePoints([[1, 1], [3, 1], [3, 3], [1, 3]], 180, [2, 2]))
