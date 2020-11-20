class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations) -> int:
        n = len(stations)
        if len(stations) == 0:
            return 0 if target <= startFuel else -1
        x = startFuel
        ans = 0
        s = set()
        while x < target:
            i = 0
            maxIdx = -1
            while i < n and stations[i][0] <= x:
                if i not in s and (maxIdx == -1 or stations[i][1] > stations[maxIdx][1]):
                    maxIdx = i
                i += 1
            if maxIdx == -1:
                return -1
            x += stations[maxIdx][1]
            ans += 1
            s.add(maxIdx)
        return ans


s = Solution()
print(s.minRefuelStops(1000000,
                       70768,
                       [[12575, 171159], [81909, 101253], [163732, 164401], [190025, 65493],
                        [442889, 31147], [481202, 166081], [586028, 206379], [591952, 52748],
                        [595013, 9163], [611883, 217156]]))
# print(s.minRefuelStops(1000,
#                        83,
#                        [[25, 27], [36, 187], [140, 186], [378, 6], [492, 202],
#                         [517, 89], [579, 234], [673, 86], [808, 53], [954, 49]]))
# print(s.minRefuelStops(1000,
#                        299,
#                        [[13, 21], [26, 115], [100, 47], [225, 99], [299, 141],
#                         [444, 198], [608, 190], [636, 157], [647, 255], [841, 123]]))
# print(s.minRefuelStops(1000,
#                        83,
#                        [[47, 220], [65, 1], [98, 113], [126, 196], [186, 218], [320, 205], [686, 317], [707, 325],
#                         [754, 104], [781, 105]]))
# print(s.minRefuelStops(100, 1, [[10, 100]]))
# print(s.minRefuelStops(100, 10, [[10, 60], [20, 20], [60, 40]]))
# print(s.minRefuelStops(100, 50, [[25, 25], [50, 50]]))
# print(s.minRefuelStops(999, 1000, [[5, 100], [997, 100], [998, 100]]))
