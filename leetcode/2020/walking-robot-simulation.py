class Solution:
    def robotSim(self, commands, obstacles) -> int:
        s = set([(x, y) for [x, y] in obstacles])
        direct = [[0, 1], [-1, 0], [0, -1], [1, 0]]
        res = 0
        i = 0
        x, y = 0, 0
        for c in commands:
            if c == -2:
                i = (i + 1) % 4
            elif c == -1:
                i = (i + 3) % 4
            else:
                k = 0
                while k < c and (x + direct[i][0], y + direct[i][1]) not in s:
                    x, y = x + direct[i][0], y + direct[i][1]
                    res = max(res, x ** 2 + y ** 2)
                    k += 1
        return res


s = Solution()
print(s.robotSim([4, -1, 4, -2, 4], [[2, 4]]))
