import collections


class Solution:
    def countPairs(self, a) -> int:
        mod = 10 ** 9 + 7
        power2 = [2 ** i for i in range(41)]
        count = collections.Counter(a)
        res = 0
        for k in count:
            for p in power2:
                if k == p - k:
                    res += (count[k] * (count[k] - 1) // 2) % mod
                elif k < p - k:
                    res += (count[k] * count.get(p - k, 0)) % mod
        return res


s = Solution()
print(s.countPairs([1, 3, 5, 7, 9]))
print(s.countPairs([1, 1, 1, 3, 3, 3, 7]))
