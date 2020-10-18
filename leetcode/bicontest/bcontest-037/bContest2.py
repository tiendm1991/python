import math


class Solution:
    def bestCoordinate(self, towers, radius: int):
        towers.sort()
        ans, _max = 0, 0
        rSquare = radius ** 2
        n = len(towers)
        for i in range(n):
            count = 0
            for j in range(n):
                dSquare = (towers[i][0] - towers[j][0]) ** 2 + (towers[i][1] - towers[j][1]) ** 2
                if dSquare <= rSquare:
                    count += towers[j][2] // (1 + math.sqrt(dSquare))
            if count > _max:
                ans = i
                _max = count
        return [towers[ans][0], towers[ans][1]]


s = Solution()
print(s.bestCoordinate(
    [[28, 6, 30], [23, 16, 0], [21, 42, 22], [50, 33, 34], [14, 7, 50], [40, 31, 4], [39, 45, 17], [46, 21, 12],
     [45, 36, 45], [35, 43, 43], [29, 41, 48], [22, 27, 5], [42, 44, 45], [10, 49, 50], [47, 43, 26], [40, 36, 25],
     [10, 25, 6], [27, 30, 30], [50, 35, 20], [11, 0, 44], [34, 29, 28]], 12))
