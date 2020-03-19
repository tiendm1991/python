from datetime import datetime, time
import heapq
import math

class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        result = [-1] * (2 * n)
        nums += nums
        stack = [0]
        cur = 1
        while cur < 2 * n:
            x = nums[cur]
            while stack and nums[stack[-1]] < x:
                result[stack.pop()] = nums[cur]
            stack.append(cur)
            cur += 1
        return result[:n]


s = Solution()
startTime = datetime.now()
print(s.nextGreaterElements([1,2,1,3,2,1]))
print(datetime.now() - startTime)

