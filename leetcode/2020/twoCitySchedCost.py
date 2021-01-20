class Solution:
    def twoCitySchedCost1(self, costs) -> int:
        _max = 10 ** 9 + 7
        n = len(costs) // 2
        dp = [[_max for j in range(2 * n + 1)] for i in range(2 * n + 1)]
        dp[0][0] = 0
        for i in range(1, 2 * n + 1):
            c = costs[i - 1]
            for j in range(i + 1):
                dp[i][j] = min(dp[i - 1][j - 1] + c[0], dp[i - 1][j] + c[1])
        return dp[2 * n][n]

    def twoCitySchedCost(self, costs) -> int:
        allA = sum([x[0] for x in costs])
        getB = sorted([x[1] - x[0] for x in costs])
        return allA + sum(getB[:(len(costs) // 2)])


s = Solution()
print(s.twoCitySchedCost([[29, 70], [48, 5], [96, 67], [14, 13], [84, 18], [57, 46]]))
