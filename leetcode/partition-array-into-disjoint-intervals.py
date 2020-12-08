class Solution:
    def partitionDisjoint(self, a) -> int:
        n = len(a)
        _max = a[::]
        res = n
        for i in range(1, n):
            _max[i] = max(_max[i - 1], _max[i])
        m = a[-1]
        for i in range(n - 2, -1, -1):
            if m >= _max[i]:
                res = i + 1
            m = min(m, a[i])
        return res


s = Solution()
print(s.partitionDisjoint([1, 1, 1, 0, 6, 12]))
print(s.partitionDisjoint([5, 0, 3, 8, 6]))
