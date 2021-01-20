import collections


class Solution:
    def canReorderDoubled(self, a) -> bool:
        d = collections.Counter(a)
        keys = sorted([k for k in d], key=lambda x: abs(x))
        for k in keys:
            if d[k] == 0:
                continue
            remain = d.get(2 * k, 0) - d.get(k)
            if remain < 0:
                return False
            d[2 * k] = remain
        return True


s = Solution()
print(s.canReorderDoubled([-4, 2, 4, -2]))
print(s.canReorderDoubled([1, 2, 3, 6]))
