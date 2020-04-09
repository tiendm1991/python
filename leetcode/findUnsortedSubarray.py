class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        n = len(nums)
        if n < 2:
            return 0
        if n == 2:
            return 0 if nums[0] <= nums[1] else 2
        start, end = 1, n-2
        while start < n and nums[start] >= nums[start-1]:
            start += 1
        while end >= 0 and nums[end] <= nums[end+1]:
            end -= 1
        start -= 1
        end += 1
        if start == n - 1 and end == 0:
            return 0
        elif start > end:
            return start - end + 1
        else:
            s = nums[start:end+1]
            _min, _max = min(s), max(s)
            while start >= 0 and nums[start] > _min:
                start -= 1
            while end < n and nums[end] < _max:
                end += 1
            return end - start - 1

s = Solution()
print(s.findUnsortedSubarray([1,3,2,4]))