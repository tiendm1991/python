class Solution:
    def numMovesStonesII(self, a):
        n = len(a)
        a.sort()
        low, high = n, 0
        if a[-1] - a[0] + 1 == n:
            return [low, high]
        high = max(a[-1] - a[1] + 1 - (n - 1), a[-2] - a[0] + 1 - (n - 1))

        return [low, high]


s = Solution()
print(s.numMovesStonesII([4, 7, 9]))  # 1,2
print(s.numMovesStonesII([3, 4, 5, 6, 10]))  # 2,3
print(s.numMovesStonesII([1, 3, 4, 5, 10]))  # 1, 4
print(s.numMovesStonesII([4, 5, 9]))  # 2,3
