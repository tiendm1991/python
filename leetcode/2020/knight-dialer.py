# 1 2 3
# 4 5 6
# 7 8 9
# # 0 #
class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        mod = 10 ** 9 + 7
        canJump = {0: [4, 6],
                   1: [6, 8],
                   2: [7, 9],
                   3: [4, 8],
                   4: [0, 3, 9],
                   5: [],
                   6: [0, 1, 7],
                   7: [2, 6],
                   8: [1, 3],
                   9: [2, 4]}
        dp = [[1 if i == 0 else 0 for j in range(10)] for i in range(n)]
        for i in range(1, n):
            for j in range(10):
                dp[i][j] = sum([dp[i - 1][p] for p in canJump[j]]) % mod
        return sum(dp[n - 1]) % mod


s = Solution()
print(s.knightDialer(2))
print(s.knightDialer(3))
print(s.knightDialer(4))
