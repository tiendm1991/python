from datetime import datetime


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        dp = [[i + j for j in range(n2 + 1)] for i in range(n1 + 1)]
        for i in range(1, n1 + 1):
            c1 = word1[i - 1]
            for j in range(1, n2 + 1):
                c2 = word2[j - 1]
                if c1 == c2:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])
        return dp[n1][n2]


s = Solution()
startTime = datetime.now()
print(s.minDistance("horse", "ros"))
print(datetime.now() - startTime)
