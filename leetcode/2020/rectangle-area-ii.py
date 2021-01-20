class Solution:
    def rectangleArea(self, a) -> int:
        mod = 10 ** 9 + 7
        n = len(a)
        if n == 1:
            return ((a[0][3] - a[0][1]) * (a[0][2] - a[0][0])) % mod
        y = sorted(set([r[1] for r in a] + [r[3] for r in a]))
        ans = 0
        for idx in range(len(y) - 1):
            l = []
            for i in range(n):
                r = a[i]
                if r[1] <= y[idx] and y[idx + 1] <= r[3]:
                    l.append([r[0], r[2]])
            if not l:
                continue
            l = sorted(l, key=lambda x: x[0])
            x = 0
            x = (x + l[0][1] - l[0][0]) % mod
            pre = l[0][1]
            for i in range(1, len(l)):
                x = (x + max(0, l[i][1] - max(l[i][0], pre))) % mod
                pre = max(pre, l[i][1])
            ans = (ans + x * (y[idx + 1] - y[idx])) % mod
        return ans


s = Solution()
print(s.rectangleArea([[49, 40, 62, 100], [11, 83, 31, 99], [19, 39, 30, 99]]))
print(s.rectangleArea([[0, 0, 1000000000, 1000000000]]))
print(s.rectangleArea([[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]))
