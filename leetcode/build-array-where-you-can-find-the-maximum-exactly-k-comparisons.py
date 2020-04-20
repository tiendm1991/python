from datetime import datetime
import math

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        if k == 0 or k > n or k > m:
            return 0
        mod = 10 ** 9 + 7
        dp = [[[0 for a in range(k+1)] for i in range(m + 1)] for j in range(n+1)]
        for i in range(1, m+1):
            dp[1][i][1] = 1
        for a in range(2, n+1):
            for b in range(1, m+1):
                for c in range(1, k+1):
                    # max = b and nums[a] < b => max is previous => c not change
                    # => dp[a][b][c] = sumOfAll(dp[a-1][b][c])(b - 1 step) = (b-1) * dp[a-1][b][c] (1)
                    # for x in range(1, b):
                    #     dp[a][b][c] += dp[a-1][b][c] % mod
                    # max = b and nums[a] == b. If max(1...a-1) == b => c not change => dp[a][b][c] += dp[a-1][b][c] (2)
                    # (1) + (2) => dp[a][b][c] = b * dp[a-1][b][c]
                    dp[a][b][c] = (dp[a - 1][b][c] * b) % mod
                    # max = b and nums[a] == b. If max(1...a-1) < b => c change
                    # => dp[a][b][c] = sumOfAll(dp[a-1][x][c-1]) (with x from 1...b-1)
                    for x in range(1, b):
                        dp[a][b][c] += dp[a-1][x][c-1] % mod
        result = 0
        for i in range(1, m+1):
            result = (result + dp[n][i][k]) % mod
        return result
pattern = Solution()
startTime = datetime.now()
print(pattern.numOfArrays(1, 2, 1))
print(pattern.numOfArrays(2, 3, 1))
print(pattern.numOfArrays(3, 3, 1))
print(pattern.numOfArrays(4, 3, 3))
print(pattern.numOfArrays(5, 3, 3))
print(pattern.numOfArrays(37, 17, 7))
print(datetime.now() - startTime)