class Solution:
    def maxCoins_topdown(self, nums) -> int:
        dp = {}

        def helper(a):
            n = len(a)
            if n == 0:
                return 0
            if n == 1:
                return a[0]
            if a in dp:
                return dp[a]
            res = 0
            for i in range(n):
                left, right = 1 if i == 0 else a[i - 1], 1 if i == n - 1 else a[i + 1]
                res = max(res, left * a[i] * right + helper(a[:i] + a[i + 1:]))
            dp[a] = res
            return res

        return helper(tuple(nums))

    def maxCoins(self, nums) -> int:
        n = len(nums)
        dp = [[0 for j in range(n)] for i in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                numLeft, numRight = 1 if i == 0 else nums[i - 1], 1 if j == n - 1 else nums[j + 1]
                for k in range(i, j + 1):
                    preLeft = 0 if k == 0 else dp[i][k - 1]
                    preRight = 0 if k == n - 1 else dp[k + 1][j]
                    dp[i][j] = max(dp[i][j], numLeft * nums[k] * numRight + preLeft + preRight)
        return dp[0][n - 1]


s = Solution()
print(s.maxCoins([3, 2, 5, 8]), s.maxCoins_topdown([3, 2, 5, 8]))
print(s.maxCoins([3, 1, 5, 8]), s.maxCoins_topdown([3, 1, 5, 8]))
