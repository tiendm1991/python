import collections

class Solution:
    def kLengthApart(self, nums, k: int) -> bool:
        start = -1
        n = len(nums)
        if n < 2:
            return True
        for i in range(n):
            if nums[i] == 0:
                continue
            if start != -1 and i - start <= k:
                return False
            start = i
        return True
