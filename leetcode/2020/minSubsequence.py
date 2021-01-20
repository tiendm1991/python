import collections


class Solution:
    def minSubsequence(self, nums):
        target = sum(nums) // 2
        s = sum(nums)
        nums = sorted(nums, reverse=True)
        top = 0
        while s > target:
            top = nums.pop()
            s -= top
        return nums + [top]


s = Solution()
print(s.minSubsequence([7, 4, 2, 8, 1, 7, 7, 10]))
