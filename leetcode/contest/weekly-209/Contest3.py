# https://leetcode.com/problems/maximum-number-of-visible-points/
class Solution:
    def specialArray(self, nums) -> int:
        nums.sort()
        n = len(nums)
        if n == 1:
            return 1 if nums[0] >= 1 else -1
        if nums[0] >= n:
            return n
        i = n - 1
        x = nums[-1]
        while i >= 0:
            while i >= 0 and nums[i] == x:
                i -= 1
            s = n - i - 1
            if nums[i] < s <= x:
                return s
            x = nums[i]
        return -1


s = Solution()
print(s.specialArray([0, 3, 6, 7, 7]))
# print(s.specialArray([0, 4, 3, 0, 4]))
