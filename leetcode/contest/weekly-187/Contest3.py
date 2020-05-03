import collections
from datetime import datetime


class Solution:
    def longestSubarray(self, nums, limit: int) -> int:
        n = len(nums)
        if n < 2:
            return n
        begin, end = 0, 0
        _min, _max, result = nums[0], nums[0], 0
        for i in range(1, n):
            _min = min(_min, nums[i])
            _max = max(_max, nums[i])
            end = i
            if _max - _min <= limit:
                result = max(result, end - begin + 1)
            else:
                begin = i
                if nums[i] == _min:
                    _max = nums[i]
                    while nums[begin] - nums[i] <= limit:
                        _max = max(_max, nums[begin])
                        begin -= 1
                else:
                    _min = nums[i]
                    while nums[i] - nums[begin] <= limit:
                        _min = min(_min, nums[begin])
                        begin -= 1
                begin += 1
        return result


s = Solution()
start = datetime.now()
print(s.longestSubarray([10, 1, 3, 2, 4, 7, 2, 2], 5))
print(datetime.now() - start)
