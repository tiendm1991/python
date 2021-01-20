import math


class Solution:
    def minPatches(self, nums, n: int) -> int:
        _maxCover = 1
        step = 0
        count = 0
        idx = 0
        _maxCover = 0
        while _maxCover < n:
            if idx == len(nums) or _maxCover < nums[idx] - 1:
                count += 1
                _maxCover = _maxCover * 2 + 1
            else:
                _maxCover += nums[idx]
                idx += 1
            step += 1
        return count


s = Solution()
startTime = datetime.now()
print(s.minPatches([1, 2, 2], 0))
print(datetime.now() - startTime)
