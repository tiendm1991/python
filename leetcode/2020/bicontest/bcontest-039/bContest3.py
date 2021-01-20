class Solution:
    def minimumJumps(self, forbidden, a: int, b: int, x: int) -> int:
        f = set(forbidden)
        visited = set()
        q = [(0, False)]
        ans = 0
        while q:
            newQ = []
            for v in q:
                if v[0] == x:
                    return ans
                forward = v[0] + a
                if forward not in f and (forward, True) not in visited and (
                        forward - b <= x or a < b) and forward < 10000:
                    newQ.append((forward, True))
                    visited.add((forward, True))

                if v[1]:
                    backward = v[0] - b
                    if backward not in f and (backward, False) not in visited and backward > 0:
                        newQ.append((backward, False))
                        visited.add((backward, False))
            ans += 1
            q = newQ
        return -1


s = Solution()
print(s.minimumJumps(
    [71, 924, 1718, 1458, 371, 597, 1790, 889, 414, 784, 1883, 6, 1650, 1549, 552, 1233, 1467, 1514, 1568, 211, 1301,
     772, 377, 1751, 1699, 1701, 1214, 1874, 324, 1991, 1006, 1413, 41, 289, 1274, 802, 1892, 1908, 1960, 1635, 69, 423,
     1795, 96, 1024, 1596, 1044, 1513, 1390, 711, 1806, 1298, 968, 1160, 1232, 1315, 1646, 1178, 169, 1295, 466, 44, 10,
     1250, 1283, 927, 49, 267, 1773, 342, 1828, 1949, 1291, 244, 707, 408, 798, 938, 1542, 690, 639, 1148, 1081, 431,
     752, 120, 1125, 339, 480, 247, 733, 266]
    , 806
    , 1994
    , 326))
print(s.minimumJumps([73, 200], 29, 98, 80))
print(s.minimumJumps([5, 2, 10, 12, 18], 8, 6, 16))
print(s.minimumJumps([8, 3, 16, 6, 12, 20], 15, 13, 11))
print(s.minimumJumps([14, 4, 18, 1, 15], 3, 15, 9))
