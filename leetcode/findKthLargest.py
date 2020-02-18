import functools
from datetime import datetime, time
import math

class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        n = len(nums)
        if k > n:
            return -1
        def find(nums, first, last, k):
            if first == last:
                return nums[first]
            if last - first == 1:
                return max(nums[first], nums[last]) if k == 1 else min(nums[first], nums[last])
            pivot = nums[last]
            idx = first - 1
            i = first
            while i < last:
                if nums[i] < pivot:
                    idx += 1
                    nums[i], nums[idx] = nums[idx], nums[i]
                i += 1
            idx += 1
            nums[idx], nums[last] = nums[last], nums[idx]
            if idx == first:
                if k == last - first + 1:
                    return nums[idx]
                else:
                    return find(nums, idx+1, last, k)
            if last - idx + 1 >= k:
                return find(nums, idx, last, k)
            else:
                return find(nums, first, idx - 1, k - (last - idx + 1))
        return find(nums, 0, n-1, k)




s = Solution()
startTime = datetime.now()
print(s.findKthLargest([3,3,3,3,3,3,3,3,3],
1))
print(datetime.now() - startTime)

