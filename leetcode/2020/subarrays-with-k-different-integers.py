import collections


class Solution:
    def subarraysWithKDistinct(self, a, k) -> int:
        n = len(a)
        if n == 1:
            return 1

        def longestSubArrWithLengthK(k):
            counter = {}
            i, j = 0, 0
            dp = [0] * n
            while j < n:
                counter[a[j]] = counter.get(a[j], 0) + 1
                while i < j and len(counter) > k:
                    if counter[a[i]] == 1:
                        del counter[a[i]]
                    else:
                        counter[a[i]] -= 1
                    i += 1
                if len(counter) == k:
                    dp[j] = j - i + 1
                j += 1
            return dp

        dp1, dp2 = longestSubArrWithLengthK(k), longestSubArrWithLengthK(k - 1)
        return sum([max(dp1[i] - dp2[i], 0) for i in range(n)])


s = Solution()
print(s.subarraysWithKDistinct([1, 2, 1, 2, 3], 2))
print(s.subarraysWithKDistinct([1, 2, 1, 3, 4], 3))
print(s.subarraysWithKDistinct([5, 7, 5, 2, 3, 3, 4, 1, 5, 2, 7, 4, 6, 2, 3, 8, 4, 5, 7], 7))
