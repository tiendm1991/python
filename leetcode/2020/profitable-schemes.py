class Solution:
    def profitableSchemes1(self, G: int, P: int, group, profit) -> int:
        mod = 10 ** 9 + 7
        a = list(zip(group, profit))
        n = len(a)
        dp = [[0 for j in range(G + 1)] for i in range(P + 1)]
        dp[0][0] = 1
        for g, p in a:
            for i in range(P, -1, -1):
                for j in range(G - g, -1, -1):
                    dp[min(i + p, P)][j + g] = (dp[min(i + p, P)][j + g] + dp[i][j]) % mod
        return sum(dp[P]) % mod

    def profitableSchemes(self, G: int, P: int, group, profit) -> int:
        mod = 10 ** 9 + 7
        a = list(zip(group, profit))
        n = len(a)
        dp = [[0 for j in range(G + 1)] for i in range(P + 1)]
        dp[0][0] = 1
        for g, p in a:
            for i in range(P, -1, -1):
                for j in range(G, g - 1, -1):
                    dp[i][j] = (dp[i][j] + dp[max(i - p, 0)][j - g]) % mod
        return sum(dp[P]) % mod


s = Solution()
print(s.profitableSchemes(10, 5, [2, 3, 5], [6, 7, 8]))
