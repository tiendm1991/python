class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx > sx and ty > sy:
            if tx > ty:
                tx %= ty
            else:
                ty %= tx
        if tx < sx or ty < sy:
            return False
        if tx == sx:
            return (ty - sy) % sx == 0
        return (tx - sx) % sy == 0


s = Solution()
print(s.reachingPoints(2, 3, 41, 57))
print(s.reachingPoints(1, 2, 19, 27))
print(s.reachingPoints(3, 3, 12, 9))
print(s.reachingPoints(35, 13, 455955547, 420098884))
