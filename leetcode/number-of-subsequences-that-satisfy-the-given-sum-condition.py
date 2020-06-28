import random
import bisect


class Solution:
    def numSubseq(self, nums, target: int) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        nums.sort()
        ans = 0

        def biSearch(low, high, x):
            if low == n:
                return low
            if x + nums[low] > target:
                return low
            mid = (low + high) // 2
            if x + nums[mid] <= target:
                return biSearch(mid + 1, high, x)
            else:
                return biSearch(low, mid, x)

        for i, x in enumerate(nums):
            if 2 * x > target:
                break
            ans += 1
            j = biSearch(i + 1, n, x)
            ans = (ans + (2 ** (j - i - 1) - 1) % mod) % mod
        return ans


s = Solution()
print(s.numSubseq([3, 5, 6, 7], 9))
print(s.numSubseq([5, 2, 4, 1, 7, 6, 8], 16))
print(s.numSubseq(
    [14, 4, 6, 6, 20, 8, 5, 6, 8, 12, 6, 10, 14, 9, 17, 16, 9, 7, 14, 11, 14, 15, 13, 11, 10, 18, 13, 17, 17, 14, 17, 7,
     9, 5, 10, 13, 8, 5, 18, 20, 7, 5, 5, 15, 19, 14], 22))
