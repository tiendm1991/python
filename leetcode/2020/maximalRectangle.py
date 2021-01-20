from datetime import datetime


class Solution:
    def maximalRectangle(self, matrix):
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if i == 0:
                    dp[i][j] = int(matrix[i][j])
                    continue
                if matrix[i][j] == '1':
                    dp[i][j] = dp[i - 1][j] + 1
        for a in dp:
            a.append(0)
            stack = []
            for i in range(n + 1):
                while stack and a[stack[-1]] >= a[i]:
                    h = a[stack.pop()]
                    w = i if not stack else i - 1 - stack[-1]
                    res = max(res, h * w)
                stack.append(i)
        return res


s = Solution()
start = datetime.now()
print(s.maximalRectangle([
    ["1", "0", "1", "0", "1"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]))
print(datetime.now() - start)
