class Solution:
    def createTargetArray(self, nums, index):
        result = []
        for i in range(len(nums)):
            result.insert(index[i], nums[i])
        return result

s = Solution()
print(s.luckyNumbers())