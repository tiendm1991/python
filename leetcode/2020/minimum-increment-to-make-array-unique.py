class Solution:
    def minIncrementForUnique(self, a) -> int:
        a.sort()
        res = 0
        for i in range(1, len(a)):
            if a[i] <= a[i - 1]:
                res += a[i - 1] + 1 - a[i]
                a[i] = a[i - 1] + 1
        return res


s = Solution()
print(s.minIncrementForUnique([1, 2, 2]))
print(s.minIncrementForUnique([3, 2, 1, 2, 1, 7]))
