#https://leetcode.com/problems/distinct-subsequences/
from datetime import datetime


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ls = len(s)
        lt = len(t)
        if ls == 0 or ls < lt:
            return 0
        dp = [[0 if j > 0 else 1 for i in range(ls+1)] for j in range(lt+1)]
        for i in range(1, lt+1):
            ct = t[i-1]
            for j in range(1, ls+1):
                cs = s[j-1]
                if cs != ct:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
        return dp[lt][ls]


s = Solution()
start = datetime.now()
print(s.numDistinct('rabbbit', 'rabbit'))
print(datetime.now() - start)

