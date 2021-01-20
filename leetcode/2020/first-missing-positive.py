class Solution:
    def firstMissingPositive(self, nums) -> int:
        n = len(nums)
        if n == 0:
            return 1
        MAX = max(nums)
        if MAX <= 0:
            return 1
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = MAX
        for i in range(n):
            x = abs(nums[i])
            if x <= n and nums[x - 1] > 0:
                nums[x - 1] = -nums[x - 1]
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1


s = Solution()
print(s.firstMissingPositive([1, 2, 0]))
print(s.firstMissingPositive([3, 4, -1, 1]))
print(s.firstMissingPositive([7, 8, 9, 11, 12]))
