class Solution:
    def stoneGameVI(self, a, b) -> int:
        n = len(a)
        sa, sb = sum(a), sum(b)
        s = sorted([(a[i] + b[i], a[i], b[i]) for i in range(n)], reverse=True)
        for i, x in enumerate(s):
            if i % 2 == 0:
                sb -= x[2]
            else:
                sa -= x[1]
        if sa > sb:
            return 1
        elif sa < sb:
            return -1
        return 0

s = Solution()
print(s.stoneGameVI([1, 3], [2, 1]))
print(s.stoneGameVI([1, 2], [3, 1]))
print(s.stoneGameVI([2, 4, 3], [1, 6, 7]))
