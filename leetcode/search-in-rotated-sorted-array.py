class Solution:
    def search(self, a, target: int) -> int:
        n = len(a)
        if n == 0:
            return -1
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if a[m] == target:
                return m
            if a[l] <= a[m]:
                if a[l] <= target <= a[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if a[m] <= target <= a[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1


s = Solution()
print(s.search([5, 1, 3], 3))
print(s.search([1, 3], 3))
print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
