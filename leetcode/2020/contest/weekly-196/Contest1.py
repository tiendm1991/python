class Solution:
    def getLastMoment(self, n: int, left, right) -> int:
        return n - min(min(left), min(right))


s = Solution()
print(s.getLastMoment(4, [3, 4], [0, 1]))
