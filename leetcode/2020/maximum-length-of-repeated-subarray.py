class Solution:
    def findLength(self, a, b) -> int:
        na, nb = len(a), len(b)
        dp = [[0 for i in range(nb + 1)] for j in range(na + 1)]
        _max = 0
        for i in range(1, na + 1):
            for j in range(1, nb + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    _max = max(_max, dp[i][j])
        return _max


s = Solution()
print(s.findLength([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]))
