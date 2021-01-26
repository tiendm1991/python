class Solution:
    def numMovesStones(self, a: int, b: int, c: int):
        a, b, c = sorted([a, b, c])
        _min = 2
        if b == a + 1 == c - 1:
            _min = 0
        elif b - a <= 2 or c - b <= 2:
            _min = 1
        _max = b - 1 - a + c - 1 - b
        return [_min, _max]


s = Solution()
print(s.numMovesStones(1, 2, 5))
print(s.numMovesStones(4, 3, 2))
