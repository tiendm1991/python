class Solution:
    def find132patternSLow(self, nums) -> bool:
        n = len(nums)
        if n < 3:
            return False
        for i in range(2, n):
            s1, s2 = -1, -1
            for j in range(i):
                if nums[j] < nums[i] and s1 == -1:
                    s1 = j
                elif nums[j] > nums[i]:
                    s2 = j
            if s1 > -1 and s2 > -1 and s1 < s2:
                return True
        return False

    def find132pattern(self, nums) -> bool:
        n = len(nums)
        if n < 3:
            return False
        stack = [nums[-1]]
        s2 = None
        for i in range(n - 2, -1, -1):
            while stack and stack[-1] < nums[i]:
                s2 = stack.pop()
            if s2 is not None and nums[i] < s2:
                return True
            if not stack or stack[-1] > nums[i]:
                stack.append(nums[i])
        return False


s = Solution()
print(s.find132pattern([-2, 1, 1]))
print(s.find132pattern([42, 43, 6, 12, 3, 4, 6, 11, 20]))
print(s.find132pattern([18, 43, 11, 12, 3, 4, 6, 11, 20]))
print(s.find132pattern([-2, 1, 2, -2, 1, 2]))
print(s.find132pattern([9, 12, 13, 4, 7, 8, 5, 3, 2]))
print(s.find132pattern([1, 4, 5, -3, -1, -2]))
print(s.find132pattern([-2, 1, -2]))
print(s.find132pattern([1, 2, 3, 4]))
print(s.find132pattern([-1, 3, 2, 0]))
print(s.find132pattern([3, 1, 4, 2]))
