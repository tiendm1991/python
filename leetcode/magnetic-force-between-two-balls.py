class Solution:
    def maxDistance(self, a, m) -> int:
        n = len(a)
        a.sort()

        def check(d):
            start = 0
            m2 = m - 2
            for i in range(1, n):
                if m2 == 0:
                    return a[-1] - a[start] >= d
                if a[i] - a[start] >= d:
                    start = i
                    m2 -= 1
            return False

        left, right = 1, a[-1] - a[0]
        while left < right:
            mid = (left + right + 1) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1
        return left


s = Solution()
print(s.maxDistance([1, 2, 3, 4, 7], 3))
