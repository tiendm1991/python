class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:

        def count(x):
            ans = 0
            for i in range(1, m + 1):
                ans += min(x // i, n)
            return ans

        left, right = 1, m * n
        while left < right:
            mid = (left + right) // 2
            if count(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left
