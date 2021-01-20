import math


class Solution:
    def numPoints(self, points, r: int) -> int:
        n = len(points)
        d = 2 * r
        if n < 2:
            return n

        def distance(p1, p2):
            return math.sqrt((p1[1] - p2[1]) ** 2 + (p1[0] - p2[0]) ** 2)

        def findCenter(p1, p2):
            q = distance(p1, p2)
            if q > d:
                return [False, None, None]
            x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
            x3, y3 = (x1 + x2) / 2, (y1 + y2) / 2
            c1 = [x3 + math.sqrt(r ** 2 - (q / 2) ** 2) * (y1 - y2) / q,
                  y3 + math.sqrt(r ** 2 - (q / 2) ** 2) * (x2 - x1) / q]
            c2 = [x3 - math.sqrt(r ** 2 - (q / 2) ** 2) * (y1 - y2) / q,
                  y3 - math.sqrt(r ** 2 - (q / 2) ** 2) * (x2 - x1) / q]
            return [True, c1, c2]

        _max = 1
        for i in range(n - 1):
            for j in range(i + 1, n):
                c = findCenter(points[i], points[j])
                if c[0] is False:
                    continue
                count1, count2 = 2, 2
                for k in range(n):
                    if k == i or k == j:
                        continue
                    if distance(c[1], points[k]) <= r:
                        count1 += 1
                    if distance(c[2], points[k]) <= r:
                        count2 += 1
                _max = max(_max, count1, count2)
        return _max


s = Solution()
print(s.numPoints([[-3, 0], [3, 0], [2, 6], [5, 4], [0, 9], [7, 8]], 5))
