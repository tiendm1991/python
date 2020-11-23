class Solution:
    def profitableSchemes(self, G: int, P: int, group, profit) -> int:
        mod = 10 ** 9 + 7
        a = list(zip(group, profit))
        n = len(a)
        dp = [[1 if i == 0 else 0 for j in range(G + 1)] for i in range(P)]
        for k in range(n):
            g, p = group[k], profit[k]
            for i in range(P + 1):
                for j in range(G - g + 1):
                    dp[min(i + p, P)][j + g] = (dp[i + p][j + g] + dp[i][j]) % mod
        return dp


s = Solution()
print(s.profitableSchemes(5, 3, [2, 3, 5], [6, 7, 8]))
