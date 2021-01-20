class Solution:
    def numSubarrayBoundedMax(self, a, L: int, R: int) -> int:
        n = len(a)
        ans = 0
        idx = -1  # last index x satisfy that x > R
        idx2 = -1  # last index x satisfy that L <= x <= R
        for i in range(n):
            if a[i] > R:
                idx = i
                idx2 = i
            elif a[i] >= L:
                ans += i - idx
                idx2 = i
            else:
                ans += idx2 - idx

        return ans


s = Solution()
print(s.numSubarrayBoundedMax([2, 1, 4, 3], 2, 3))
print(s.numSubarrayBoundedMax([1, 4, 3, 1, 5], 2, 4))
print(s.numSubarrayBoundedMax([2, 1, 4, 2, 3, 1, 5], 2, 4))
