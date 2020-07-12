import math


class Solution:
    def getMinDistSum(self, positions) -> float:
        n = len(positions)
        x = sum([p[0] for p in positions]) / n
        y = sum([p[1] for p in positions]) / n
        epsilon = 1 / (10 ** 9)
        center = (x, y)
        prev = None

        def dis(p1, p2):
            return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

        while prev is None or dis(center, prev) > epsilon:
            prev = center
            upx, downx, upy, downy = 0, 0, 0, 0
            for p in positions:
                d = dis(center, p)
                if d == 0:
                    continue
                upx += p[0] / d
                downx += 1 / d
                upy += p[1] / d
                downy += 1 / d
            if downx == 0 or downy == 0:
                break
            center = (upx / downx, upy / downy)

        result = 0
        for p in positions:
            result += dis(p, center)
        return result

s = Solution()
print(s.getMinDistSum([[0, 1], [3, 2], [4, 5], [7, 6], [8, 9], [11, 1], [2, 12]]))
