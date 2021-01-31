class Solution:
    def canEat(self, candiesCount, queries):
        n = len(candiesCount)
        pre = [0] * (n + 1)
        for i in range(1, n + 1):
            pre[i] = pre[i - 1] + candiesCount[i - 1]

        def check(t, d, c):
            # if pre[t + 1] < d + 1:
            #     return False
            # if c * (d + 1) <= pre[t]:
            #     return False
            return pre[t + 1] >= d + 1 and c * (d + 1) > pre[t]

        res = [False] * len(queries)
        for i, q in enumerate(queries):
            res[i] = check(q[0], q[1], q[2])
        return res


s = Solution()
print(s.canEat([7, 4, 5, 3, 8], [[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]]))
print(s.canEat(
    [16, 38, 8, 41, 30, 31, 14, 45, 3, 2, 24, 23, 38, 30, 31, 17, 35, 4, 9, 42, 28, 18, 37, 18, 14, 46, 11, 13, 19,
     3,
     5, 39, 24, 48, 20, 29, 4, 19, 36, 11, 28, 49, 38, 16, 23, 24, 4, 22, 29, 35, 45, 38, 37, 40, 2, 37, 8, 41, 33,
     8,
     40, 27, 13, 4, 33, 5, 8, 14, 19, 35, 31, 8, 8],
    [[43, 1054, 49]]))
