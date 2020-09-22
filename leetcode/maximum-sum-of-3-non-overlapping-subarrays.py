class Solution:
    def maxSumOfThreeSubarrays(self, nums, k: int):
        n = len(nums)
        s = [0] * n
        s[0] = sum(nums[:k])
        for i in range(1, n - k + 1):
            s[i] = s[i - 1] - nums[i - 1] + nums[i + k - 1]
        dp1 = [0] * n
        for i in range(0, n):
            if s[i] != 0:
                if s[i] > s[dp1[i - 1]]:
                    dp1[i] = i
                else:
                    dp1[i] = dp1[i - 1]
        dp2 = [[-1, -1] for i in range(n)]
        dp2[k] = [dp1[0], k]
        for i in range(k + 1, n):
            if s[i] + s[dp1[i - k]] > s[dp2[i - 1][0]] + s[dp2[i - 1][1]]:
                dp2[i] = [dp1[i - k], i]
            else:
                dp2[i] = dp2[i - 1]
        dp3 = [[-1, -1, -1] for i in range(n)]
        dp3[2 * k] = [dp2[k][0], dp2[k][1], 2 * k]
        for i in range(2 * k + 1, n):
            if s[i] + s[dp2[i - k][0]] + s[dp2[i - k][1]] > s[dp3[i - 1][0]] + s[dp3[i - 1][1]] + s[dp3[i - 1][2]]:
                dp3[i] = [dp2[i - k][0], dp2[i - k][1], i]
            else:
                dp3[i] = dp3[i - 1]
        return dp3[n-1]


s = Solution()
print(s.maxSumOfThreeSubarrays([1, 2, 1, 2, 6, 7, 5, 1], 2))
