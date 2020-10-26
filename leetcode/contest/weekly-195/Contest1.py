class Solution:
    def isPathCrossing(self, path: str) -> bool:
        s = {(0, 0)}
        cur = (0, 0)
        for p in path:
            x, y = cur[0], cur[1]
            if p == 'N':
                y += 1
            elif p == 'E':
                x += 1
            elif p == 'W':
                x -= 1
            else:
                y -= 1
            cur = (x, y)
            if cur in s:
                return True
            s.add(cur)
        return False


s = Solution()
print(s.isPathCrossing('NESW'))
