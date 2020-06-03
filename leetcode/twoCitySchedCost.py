class Solution:
    def twoCitySchedCost1(self, costs) -> int:
        _max = 10 ** 9 + 7
        n = len(costs) // 2
        dp = [[_max for j in range(2 * n + 1)] for i in range(2 * n + 1)]
        dp[0][0] = 0
        for i in range(1, 2 * n + 1):
            c = costs[i-1]
            for j in range(i + 1):
                dp[i][j] = min(dp[i-1][j-1] + c[0], dp[i-1][j] + c[1])
        return dp[2 * n][n]

    def twoCitySchedCost(self, costs) -> int:
        _max = 10 ** 9 + 7
        n = len(costs) // 2
        dp = [[_max for j in range(2 * n + 1)] for i in range(2 * n + 1)]
        dp[0][0] = 0
        for i in range(1, 2 * n + 1):
            c = costs[i-1]
            for j in range(i + 1):
                dp[i][j] = min(dp[i-1][j-1] + c[0], dp[i-1][j] + c[1])
        return dp[2 * n][n]
s = Solution()
print(s.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))