import functools
from datetime import datetime, time
import math


class Solution:
    def longestIncreasingPath(self, matrix) -> int:
        _max = 1
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        queue = set()
        for i in range(m):
            for j in range(n):
                if i-1 >= 0 and matrix[i-1][j] > matrix[i][j]:
                    continue
                if i+1 < m and matrix[i+1][j] > matrix[i][j]:
                    continue
                if j-1 >= 0 and matrix[i][j-1] > matrix[i][j]:
                    continue
                if j+1 < n and matrix[i][j+1] > matrix[i][j]:
                    continue
                dp[i][j] = 1
                queue.add(i * n + j)
        while len(queue) > 0:
            newQueue = set()
            for q in queue:
                i, j = q // n, q % n
                if i-1 >= 0 and matrix[i-1][j] < matrix[i][j]:
                    dp[i-1][j] = max(dp[i-1][j], dp[i][j] + 1)
                    newQueue.add(j + n * (i-1))
                if i+1 < m and matrix[i+1][j] < matrix[i][j]:
                    dp[i+1][j] = max(dp[i+1][j], dp[i][j] + 1)
                    newQueue.add(j + n * (i+1))
                if j-1 >= 0 and matrix[i][j-1] < matrix[i][j]:
                    dp[i][j-1] = max(dp[i][j-1], dp[i][j] + 1)
                    newQueue.add(j- 1 + n * i)
                if j+1 < n and matrix[i][j+1] < matrix[i][j]:
                    dp[i][j+1] = max(dp[i][j+1], dp[i][j] + 1)
                    newQueue.add(j + 1 + n * i)
            queue = newQueue
        return max([max(a) for a in dp])
s = Solution()
startTime = datetime.now()
print(s.longestIncreasingPath([[0],[1],[5],[5]]))
print(datetime.now() - startTime)

