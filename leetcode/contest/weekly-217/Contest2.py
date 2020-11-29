class Solution:
    def mostCompetitive(self, nums, k: int):
        n = len(nums)
        if n == k:
            return nums
        if k == 1:
            return min(nums)
        stack = []
        for i, x in enumerate(nums):
            while stack and n - 1 - i >= k - len(stack) and x < stack[-1]:
                stack.pop()
            if len(stack) < k:
                stack.append(x)
        return stack


s = Solution()
print(s.mostCompetitive([71, 18, 52, 29, 55, 73, 24, 42, 66, 8, 80, 2], 3))
# print(s.mostCompetitive([3, 5, 2, 6], 2))
# print(s.mostCompetitive([2, 4, 3, 3, 5, 4, 9, 6], 4))
