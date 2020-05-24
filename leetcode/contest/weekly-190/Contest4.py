import math


class Solution:
    def maxDotProduct(self, nums1, nums2) -> int:
        MIN = -10 ** 9 + 7
        n1, n2 = len(nums1), len(nums2)
        dp = [[MIN for j in range(n2 + 1)] for i in range(n1 + 1)]
        dp[0][0] = 0
        for i in range(1, n1 + 1):
            x = nums1[i - 1]
            for j in range(1, n2 + 1):
                y = nums2[j - 1]
                # dp[i][j] = max(x * y, dp[i - 1][j - 1] + x * y, dp[i - 1][j], dp[i][j - 1])
                dp[i][j] = max(x * y + max(dp[i - 1][j - 1], 0), dp[i - 1][j], dp[i][j - 1])
        return dp[n1][n2]


s = Solution()
print(s.maxDotProduct([-1, -1], [1, 1]))
print(s.maxDotProduct([3, -2], [2, -6, 7]))
