class Solution:
    def numMovesStonesII(self, a):
        n = len(a)
        a.sort()
        minimum, maximum = n, 0
        maximum = max(a[-1] - a[1] + 1 - (n - 1), a[-2] - a[0] + 1 - (n - 1))
        i = 0
        for j in range(n):
            while a[j] - a[i] + 1 > n:
                i += 1
            if a[j] - a[i] + 1 == j - i + 1 == n - 1:
                minimum = min(minimum, 2)
            else:
                minimum = min(minimum, n - (j - i + 1))
        return [minimum, maximum]


s = Solution()
print(s.numMovesStonesII([2, 3, 4, 7, 8, 9]))  # 2, 2
print(s.numMovesStonesII([4, 7, 9]))  # 1,2
print(s.numMovesStonesII([3, 4, 5, 6, 10]))  # 2,3
print(s.numMovesStonesII([1, 3, 4, 5, 10]))  # 1, 4
print(s.numMovesStonesII([4, 5, 9]))  # 2,3
