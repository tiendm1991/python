import collections


class Solution:
    def maximumUniqueSubarray(self, nums) -> int:
        d = collections.deque()
        s = set()
        _sum = 0
        res = 0
        for i, x in enumerate(nums):
            d.append(x)
            _sum += x
            while x in s:
                left = d.popleft()
                _sum -= left
                s.remove(left)
            res = max(res, _sum)
            s.add(x)
        return res


s = Solution()
print(s.maximumUniqueSubarray([4, 2, 4, 5, 6]))
print(s.maximumUniqueSubarray([5, 2, 1, 2, 5, 2, 1, 2, 5]))
