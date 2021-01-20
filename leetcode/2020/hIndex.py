class Solution:
    def hIndex(self, a) -> int:
        n = len(a)
        if n == 0:
            return 0

        def biSearch(low, high):
            if low > high:
                return 0
            if low == high:
                return n - high if a[high] >= n - high else 0
            mid = (low + high) // 2
            if a[mid] >= n - mid and (mid == 0 or a[mid - 1] <= n - mid):
                return n - mid
            elif a[mid] < n - mid:
                return biSearch(mid + 1, high)
            else:
                return biSearch(low, mid - 1)

        return biSearch(0, len(a) - 1)


s = Solution()
print(s.hIndex([0, 1, 2, 3, 4]))
