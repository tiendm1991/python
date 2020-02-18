import functools
from datetime import datetime, time
import math

class Solution:
    def maximalSquare(self, matrix) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        _max = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '0':
                    continue
                dp[i][j] = 1
                _max = max(_max, 1)
                if i > 1 and j > 1:
                    dp[i][j] = min([dp[i-1][j], dp[i][j-1], dp[i-1][j-1]]) + 1
                    _max = max(_max, dp[i][j])
        return _max * _max

s = Solution()
startTime = datetime.now()
print(s.maximalSquare([["0","0","0","1"],
                       ["1","1","0","1"],
                       ["1","1","1","1"],
                       ["0","1","1","1"],
                       ["0","1","1","1"]]))
print(datetime.now() - startTime)

