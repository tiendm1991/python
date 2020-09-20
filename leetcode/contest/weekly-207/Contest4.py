class Solution:
    def connectTwoGroups(self, cost) -> int:
        sz1, sz2 = len(cost), len(cost[0])
        dp = [[-1 for j in range(sz1)] for i in range(2 ** sz2)]
        min_s2 = [min([cost[i][j] for i in range(sz1)]) for j in range(sz2)]
        return min_s2

        def help(i, mask):
            if i == sz1:
                return 1
            if dp[i][mask]:
                return dp[i][mask]

        return help(0, 0)


s = Solution()
print(s.connectTwoGroups([[15, 96], [36, 2]]))
