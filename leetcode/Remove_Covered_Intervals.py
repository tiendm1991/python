import functools


class Solution:
    def removeCoveredIntervals(self, intervals) -> int:
        def cmp(a, b):
            if a[0] != b[0]:
                return a[0] - b[0]
            return b[1] - a[1]

        a = sorted(intervals, key=functools.cmp_to_key(cmp))
        ans = []
        i = 0
        while i < len(a):
            if not ans or a[i][1] > ans[-1][1]:
                ans.append(a[i])
                continue
            i += 1
        return len(ans)


s = Solution()
print(s.removeCoveredIntervals([[1, 2], [1, 4], [3, 4]]))
