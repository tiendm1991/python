import collections


class Solution:
    def maxEqualRowsAfterFlips(self, matrix) -> int:
        n = len(matrix)
        if n == 1:
            return 1
        d = collections.Counter([tuple(r) for r in matrix])
        res = 0
        for k in d:
            count = d[k]
            opposite = tuple(x ^ 1 for x in k)
            if opposite in d:
                count += d[opposite]
            res = max(res, count)
        return res


s = Solution()
print(s.maxEqualRowsAfterFlips([[0, 0, 0],
                                [0, 0, 1],
                                [1, 1, 0]]))
