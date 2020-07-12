import math


class Solution:
    def getMinDistSum(self, positions) -> float:

        x, y = None, None

        x_sum, y_sum = 0, 0
        for x, y in positions:
            x_sum += x
            y_sum += y

        x = x_sum / len(positions)
        y = y_sum / len(positions)

        def dis(a, b):
            return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

        prex, prey = float('-inf'), float('-inf')
        delte = 1 / (10 ** 8)

        while dis((x, y), (prex, prey)) > delte:
            upx, downx, upy, downy = 0, 0, 0, 0
            for px, py in positions:
                temp = dis((px, py), (x, y))
                if temp == 0:
                    continue
                upx += px / temp
                downx += 1 / temp
                upy += py / temp
                downy += 1 / temp
            if downx == 0 or downy == 0:
                break
            if downx != 0:
                newx = upx / downx
            if downy != 0:
                newy = upy / downy
            prex, prey, x, y = x, y, newx, newy

        res = 0
        for p in positions:
            res += dis(p, (x,y))

        return res


s = Solution()
print(s.getMinDistSum([[0, 1], [3, 2], [4, 5], [7, 6], [8, 9], [11, 1], [2, 12]]))
