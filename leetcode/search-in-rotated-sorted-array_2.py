class Solution:
    def search(self, a, target: int) -> bool:
        n = len(a)
        if n == 0:
            return False
        if n == 1:
            return a[0] == target
        l, r = 0, n - 1
        while l <= r:
            if a[l] == target or a[r] == target:
                return True
            m = (l + r) // 2
            if a[m] == target:
                return True
            if a[l] <= a[m]:
                if a[m] == a[r]:
                    l += 1
                    r = m - 1
                    continue
                if a[l] < target < a[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if a[m] < target < a[r]:
                    l = m + 1
                else:
                    r = m - 1
        return False


s = Solution()
print(s.search([2, 5, 6, 0, 0, 1, 2], 0))
