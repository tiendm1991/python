import collections
import functools


class Solution:
    def frequencySort(self, nums):
        d = collections.Counter(nums)

        def comp(x, y):
            if d[x] != d[y]:
                return d[x] - d[y]
            return y - x

        return sorted(nums, key=functools.cmp_to_key(comp))
