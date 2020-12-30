import math


class Solution:
    def minAreaFreeRect(self, points) -> float:
        def getCenter(a, b):
            return (a[0] + b[0]) / 2, (a[1] + b[1]) / 2

        def disSquare(a, b):
            return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2

        # def isRectangle(a, b, c, d):
        #     center = [(a[0] + b[0] + c[0] + d[0]) // 4, (a[1] + b[1] + c[1] + d[1]) // 4]
        #     da, db, dc, dd = disSquare(a, center), disSquare(b, center), disSquare(c, center), disSquare(d, center)
        #     return da == db == dc == dd

        n = len(points)
        d = {}
        res = float('inf')
        for i in range(n - 1):
            for j in range(i + 1, n):
                o = getCenter(points[i], points[j])
                if o not in d:
                    d[o] = {}
                dis = disSquare(o, points[i])
                if dis not in d[o]:
                    d[o][dis] = [(i, j)]
                else:
                    d[o][dis].append((i, j))
        for o in d:
            for dis in d[o]:
                candidate = d[o][dis]
                if len(candidate) < 2:
                    continue
                for i in range(len(candidate) - 1):
                    for j in range(i + 1, len(candidate)):
                        a1, a2 = points[candidate[i][0]], points[candidate[i][1]]
                        b1, b2 = points[candidate[j][0]], points[candidate[j][1]]
                        res = min(res, math.sqrt(disSquare(a1, b1)) * math.sqrt(disSquare(a2, b1)))
        return res if res < float('inf') else 0


s = Solution()
# print(s.minAreaFreeRect([[3, 1], [1, 1], [0, 1], [2, 1], [3, 3], [3, 2], [0, 2], [2, 3]]))
print(s.minAreaFreeRect([[1, 2], [2, 1], [1, 0], [0, 1]]))
