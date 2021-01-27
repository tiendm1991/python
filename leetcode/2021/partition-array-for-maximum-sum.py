class Solution:
    def maxSumAfterPartitioning(self, arr, k: int) -> int:
        n = len(arr)
        dp = [0 for i in range(n)]
        for i in range(n):
            _max = arr[i]
            j = i
            while 0 <= j and i - j + 1 <= k:
                _max = max(_max, arr[j])
                s = _max * (i - j + 1)
                if j - 1 >= 0:
                    s += dp[j - 1]
                dp[i] = max(dp[i], s)
                j -= 1
        return dp[n - 1]


s = Solution()
print(s.maxSumAfterPartitioning([1, 15, 7, 9, 2, 5, 10], 3))
print(s.maxSumAfterPartitioning([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4))
