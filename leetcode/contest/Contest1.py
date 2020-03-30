import collections
class Solution:
    def findLucky(self, arr) -> int:
        n = len(arr)
        if n == 0:
            return -1
        d = collections.Counter(arr)
        _max = -1
        for k in d:
            if k == d[k] and k > _max:
                _max = k
        return _max

s = Solution()
print(s.luckyNumbers())