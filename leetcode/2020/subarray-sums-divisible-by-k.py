class Solution:
    def subarraysDivByK(self, a, k) -> int:
        d = {0: 1}
        preSumMod = 0
        res = 0
        for x in a:
            preSumMod = (preSumMod + x) % k
            res += d.get(preSumMod, 0)
            d[preSumMod] = d.get(preSumMod, 0) + 1
        return res


s = Solution()
print(s.subarraysDivByK([4, 5, 0, -2, -3, 1], 5))
