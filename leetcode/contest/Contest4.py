from datetime import datetime
import math

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        if k == 0 or m < k:
            return 0
        mod = 10 ** 9 + 7
        dp = [[[0 for a in range(k+1)] for i in range(m + 1)] for j in range(n+1)]
        for a in range(n-1, -1, -1):
            for b in range(1, m+1):
                for c in range(1, k+1):
                    if c > n - a:
                        continue
                    if a == n-1:
                        if c > 1:
                            break
                        else:
                            dp[a][b][c] = b
                        continue
                    for v in range(1, m+1):
                        if v <= b:
                            dp[a][b][c] += dp[a+1][v][c]
                        else:
                            dp[a][b][c] += dp[a+1][v][c-1]
                    dp[a][b][c] %= mod
        result = 0
        for i in range(1, m+1):
            result = (result + dp[0][i][c]) % mod
        return result
pattern = Solution()
startTime = datetime.now()
print(pattern.numOfArrays(3, 3, 1))
print(datetime.now() - startTime)