from datetime import datetime, time
import heapq

class Solution:
    def totalHammingDistance(self, nums) -> int:
        n = len(nums)
        s = 0
        while True:
            _max = 0
            count = []
            for i in range(n):
                count.append(nums[i] & 1)
                nums[i] >>= 1
                _max = max(_max, nums[i])
            x = count.count(1)
            s += x * (n-x)
            if _max == 0:
                break
        return s

s = Solution()
startTime = datetime.now()
print(s.totalHammingDistance([4,14,2,3]))
print(datetime.now() - startTime)

