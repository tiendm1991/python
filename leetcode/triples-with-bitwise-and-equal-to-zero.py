class Solution:
    def countTriplets_slow(self, a) -> int:
        n = len(a)
        d = {}
        res = 0
        for i in range(n):
            for j in range(n):
                x = a[i] & a[j]
                d[x] = d.get(x, 0) + 1
        for x in d:
            for y in a:
                if x & y == 0:
                    res += d[x]
        return res

    def countTriplets(self, a) -> int:
        n = len(a)
        d = {}
        res = 0
        for i in range(n):
            for j in range(n):
                x = a[i] & a[j]
                d[x] = d.get(x, 0) + 1
        for x in d:
            for y in a:
                if x & y == 0:
                    res += d[x]
        return res


s = Solution()
print(s.countTriplets([2, 1, 3]))
