from datetime import datetime


class Solution:
    def maximalRectangle(self, matrix):
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        _max = 0
        for i in range(m):
            for j in range(n):
                if i == 0:
                    dp[i][j] = int(matrix[i][j])
                    continue
                if matrix[i][j] == '1':
                    dp[i][j] = dp[i - 1][j] + 1
        for a in dp:
            for i in range(n):
                _min = a[i]
                for j in range(i, n):
                    _min = min(_min, a[j])
                    _max = max(_max, _min * (j - i + 1))
                    if _min == 0:
                        break
        return _max


s = Solution()
start = datetime.now()
print(s.maximalRectangle([
    ["1", "0", "1", "0", "1"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]))
print(datetime.now() - start)
