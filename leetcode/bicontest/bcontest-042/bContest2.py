class Solution:
    def getSumAbsoluteDifferences(self, nums):
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(1, n + 1):
            pre[i] = pre[i - 1] + nums[i - 1]
        res = [0] * n
        for i in range(n):
            # res[i] = (i + 1) * nums[i] - pre[i + 1] + pre[-1] - pre[i + 1] - (n - i - 1) * nums[i]
            res[i] = i * nums[i] - pre[i] + pre[-1] - pre[i] - (n - i) * nums[i]
        return res


s = Solution()
print(s.getSumAbsoluteDifferences([2, 3, 5]))
print(s.getSumAbsoluteDifferences([1, 4, 6, 8, 10]))
