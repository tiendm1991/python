class Solution:
    def gridIllumination(self, n: int, lamps, queries):
        res = [0] * len(queries)
        dRow = {}
        dCol = {}
        dRight = {}
        dLeft = {}

        def addToDict(d, key, point):
            if key not in d:
                d[key] = {point}
            else:
                d[key].add(point)

        def removeFromDict(d, key, point):
            if key in d and point in d[key]:
                if len(d[key]) == 1:
                    del d[key]
                else:
                    d[key].remove(point)

        for x, y in lamps:
            p = (x, y)
            m = min(x, y)
            left = (x - m, y - m)
            m = min(x, n - 1 - y)
            right = (x - m, y + m)
            addToDict(dRow, x, p)
            addToDict(dCol, y, p)
            addToDict(dLeft, left, p)
            addToDict(dRight, right, p)

        for i, q in enumerate(queries):
            x, y = q
            m = min(x, y)
            left = (x - m, y - m)
            m = min(x, n - 1 - y)
            right = (x - m, y + m)
            if x in dRow or y in dCol or left in dLeft or right in dRight:
                res[i] = 1
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if 0 <= i < n and 0 <= j < n:
                        p = (i, j)
                        m = min(i, j)
                        l = (i - m, j - m)
                        m = min(i, n - 1 - j)
                        r = (i - m, j + m)
                        removeFromDict(dRow, i, p)
                        removeFromDict(dCol, j, p)
                        removeFromDict(dLeft, l, p)
                        removeFromDict(dRight, r, p)
        return res


s = Solution()
print(s.gridIllumination(5, [[0, 0], [4, 4]], [[1, 1], [1, 0]]))
print(s.gridIllumination(5, [[0, 0], [4, 4]], [[1, 1], [1, 1]]))
print(s.gridIllumination(5, [[0, 0], [0, 4]], [[0, 4], [0, 1], [1, 4]]))
