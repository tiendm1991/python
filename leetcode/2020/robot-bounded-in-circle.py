class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        d = [[0, 1], [-1, 0], [0, -1], [1, 0]]
        x, y = 0, 0
        i = 0
        for c in instructions:
            if c == 'G':
                x, y = x + d[i][0], y + d[i][1]
            elif c == 'L':
                i = (i + 1) % 4
            else:
                i = (i + 3) % 4
        if x == 0 and y == 0:
            return True
        elif i == 0:
            return False
        return True


s = Solution()
print(s.isRobotBounded("GG"))
print(s.isRobotBounded("GGLLGG"))
