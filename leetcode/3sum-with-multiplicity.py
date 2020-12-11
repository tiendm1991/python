class Solution:
    def threeSumMulti(self, a, target: int) -> int:
        mod = 10 ** 9 + 7
        n = len(a)
        d = [{} for i in range(n)]
        for i in range(1, n - 1):
            x = a[i]
            for j in range(i):
                d[i][x + a[j]] = d[i].get(x + a[j], 0) + 1
        res = 0
        for i in range(2, n):
            for j in range(1, i):
                res = (res + d[j].get(target - a[i], 0)) % mod
        return res


s = Solution()
print(s.threeSumMulti([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8))
