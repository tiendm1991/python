class Solution:
    def averageWaitingTime(self, a) -> float:
        res = 0
        cur = a[0][0]
        for start, prepare in a:
            cur = max(cur, start)
            cur += prepare
            res += cur - start
        return res / len(a)


s = Solution()
print(s.averageWaitingTime([[5, 2], [5, 4], [10, 3], [20, 1]]))
print(s.averageWaitingTime([[1, 2], [2, 5], [4, 3]]))
