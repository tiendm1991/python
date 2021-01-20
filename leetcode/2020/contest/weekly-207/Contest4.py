# https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/submissions/

class Solution:
    def connectTwoGroups(self, cost) -> int:
        MAX_INT = 10 ** 9
        sz1, sz2 = len(cost), len(cost[0])
        dp = [[-1 for j in range(2 ** sz2 + 1)] for i in range(sz1 + 1)]
        min_s2 = [min([cost[i][j] for i in range(sz1)]) for j in range(sz2)]

        def help(i, mask):
            if dp[i][mask] != -1:
                return dp[i][mask]
            if i < sz1:
                # if not assigned for all points in s1 => assign
                ans = MAX_INT
                for j in range(sz2):
                    ans = min(ans, cost[i][j] + help(i + 1, mask | (1 << j)))
            else:
                # if all points in s1 are assigned => assign remain point in s2
                ans = 0
                for j in range(sz2):
                    if not mask & (1 << j):
                        ans += min_s2[j]
            dp[i][mask] = ans
            return ans

        return help(0, 0)


s = Solution()
print(s.connectTwoGroups([[1, 3, 5], [4, 1, 1], [1, 5, 3]]))
