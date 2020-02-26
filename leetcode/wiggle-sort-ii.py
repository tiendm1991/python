import functools
from datetime import datetime, time
import math

class Solution:
    def wiggleSort(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            nums.sort()
            tmp = [0 for i in range(len(nums))]
            end = len(nums) - 1
            mid = end // 2
            checkMid = True
            i = 0
            while i < len(nums):
                if checkMid:
                    tmp[i] = nums[mid]
                    mid -= 1
                else:
                    tmp[i] = nums[end]
                    end -= 1
                checkMid = not checkMid
                i += 1
        for i in range(len(nums)):
            nums[i] = tmp[i]
        print(nums)
s = Solution()
startTime = datetime.now()
print(s.wiggleSort([4,5,5,6]))
print(datetime.now() - startTime)

