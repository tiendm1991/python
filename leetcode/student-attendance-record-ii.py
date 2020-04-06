from  datetime import datetime
class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[[0 for k in range(2)] for j in range(3)] for i in range(n)]
        dp[0][0][0] = 0
        dp[0][0][1] = 1
        dp[0][1][0] = 1
        dp[0][1][1] = 0
        dp[0][2][0] = 1
        dp[0][2][1] = 0
        for i in range(1, n):
            for j in range(3):
                if j == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = dp[i-1][1][0] + dp[i-1][2][0]
                elif j == 1:
                    if i < 2:
                        dp[i][j][0] = dp[i-1][1][0] + dp[i-1][2][0]
                        dp[i][j][1] = dp[i-1][0][1] + dp[i-1][1][1] + dp[i-1][2][1]
                    else:
                        dp[i][j][0] = dp[i-1][2][0] + dp[i-2][2][0]
                        dp[i][j][1] = dp[i-1][0][1] + dp[i-1][2][1] + dp[i-2][0][1] + dp[i-2][2][1]
                else:
                    dp[i][j][0] = dp[i-1][1][0] + dp[i-1][2][0]
                    dp[i][j][1] = dp[i-1][0][1] + dp[i-1][1][1] + dp[i-1][2][1]
                dp[i][j][0] %= mod
                dp[i][j][1] %= mod
        return sum([sum(x) for x in dp[-1]]) % mod

    def checkRecord2(self, n: int) -> int:
        mod = 10 ** 9 + 7
        f = [1] * (n+1)
        for i in range(n + 1):
            if i < 3:
                f[i] = 2**i
            else:
                f[i] = f[i-1] + f[i-2] + f[i-3]
            f[i] %= mod
        s = f[n]
        for i in range(1, n+1):
            x = (f[i-1] * f[n-i]) % mod
            s += x
            s %= mod
        return s

s = Solution()
startTime = datetime.now()
print(s.checkRecord(6))
print(datetime.now() - startTime)
startTime = datetime.now()
print(s.checkRecord2(6))
print(datetime.now() - startTime)