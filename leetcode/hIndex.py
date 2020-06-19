class Solution:
    def hIndex(self, a) -> int:
        n = len(a)
        if n == 0:
            return 0

        def biSearch(low, high):
            if low == high:
                return low + 1
            mid = (low + high) // 2
            if n - mid >= a[mid]:
                return biSearch(mid, high)
            else:
                return biSearch(low, mid - 1)

        return biSearch(0, len(a) - 1)


s = Solution()
print(s.hIndex([0, 1, 2, 3, 4]))
