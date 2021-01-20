class Solution:
    def minimumMountainRemovals(self, nums) -> int:
        n = len(nums)
        dp1, dp2 = [1] * n, [1] * n
        for i in range(1, n-1):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp1[i] = max(dp1[i], dp1[j] + 1)
        res = 0
        for i in range(n-2, 0, -1):
            for j in range(i+1, n):
                if nums[i] > nums[j]:
                    dp2[i] = max(dp2[i], dp2[j] + 1)
            if dp2[i] >= 2 and dp1[i] >= 2:
                res = max(res, dp1[i] + dp2[i] - 1)
        return n - res