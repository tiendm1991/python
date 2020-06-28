class Solution:
    def shuffle(self, nums, n: int):
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i+n])
        return result