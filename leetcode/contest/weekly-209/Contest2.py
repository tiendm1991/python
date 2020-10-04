import math
from builtins import range


class Solution:
    def visiblePoints(self, points, angle: int, location) -> int:
        L = points.count(location)
        p = [x for x in points if x != location]
        n = len(p)
        if n == 1:
            return 1
        ans = 1
        for i in range(n):
            x1, y1 = p[i][0] - location[0], p[i][1] - location[1]
            count = 0
            for j in range(n):
                if i == j:
                    count += 1
                    continue
                x2, y2 = p[j][0] - location[0], p[j][1] - location[1]
                ang = math.atan2(x1 * y2 - y1 * x2, x1 * x2 + y1 * y2)
                ang = round(ang * 180 / math.pi + 360) % 360
                if ang <= angle:
                    count += 1
            ans = max(ans, count)

        return ans + L


s = Solution()
print(s.visiblePoints([[1, 1], [3, 1], [3, 3], [1, 3]], 180, [2, 2]))
