class Solution:
    def orderOfLargestPlusSign(self, N: int, mines):
        a = [[1 for j in range(N)] for i in range(N)]
        for x in mines:
            a[x[0]][x[1]] = 0

        dp = [[[0, 0, 0, 0] for i in range(N)] for j in range(N)]

        for i in range(N):
            for j in range(N):
                if i == 0 and j == 0:
                    dp[i][j][0] = a[i][j]
                    dp[i][j][1] = a[i][j]
                    continue
                if a[i][j] == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = 0
                    continue
                dp[i][j][0] = 1
                dp[i][j][1] = 1
                if j > 0:
                    dp[i][j][0] += dp[i][j - 1][0]
                if i > 0:
                    dp[i][j][1] += dp[i - 1][j][1]

        ans = 0
        for i in range(N - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if i == N - 1 and j == N - 1:
                    dp[i][j][2] = a[i][j]
                    dp[i][j][3] = a[i][j]
                    ans = a[i][j]
                    continue
                if a[i][j] == 0:
                    dp[i][j][2] = 0
                    dp[i][j][3] = 0
                    continue
                dp[i][j][2] = 1
                dp[i][j][3] = 1
                if j < N - 1:
                    dp[i][j][2] += dp[i][j + 1][2]
                if i < N - 1:
                    dp[i][j][3] += dp[i + 1][j][3]
                if min(dp[i][j]) > ans:
                    ans = min(dp[i][j])
        return ans


s = Solution()
print(s.orderOfLargestPlusSign(2, [[0, 0], [0, 1], [1, 0]]))
