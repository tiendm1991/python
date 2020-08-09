# https://leetcode.com/problems/minimum-cost-to-cut-a-stick/
class Solution:
    def minCost_TopDown(self, n: int, cuts) -> int:
        dp = {}

        def f(start, end, x, y):
            if y < x:
                return 0
            ans = end - start
            if y == x:
                return ans
            if (start, end) in dp:
                return dp[(start, end)]
            _min = 10 ** 9
            for i in range(x, y + 1):
                _min = min(_min, f(start, cuts[i], x, i - 1) + f(cuts[i], end, i + 1, y))
            dp[(start, end)] = ans + _min
            return ans + _min

        cuts.sort()
        return f(0, n, 0, len(cuts) - 1)

    def minCost_Dp(self, n: int, cuts) -> int:
        MAX_INT = 10 ** 9
        cuts.sort()
        cuts = [0] + cuts + [n]
        N = len(cuts)
        dp = [[0 if j - i <= 1 else MAX_INT for j in range(N)] for i in range(N)]
        for i in range(N - 3, -1, -1):
            for j in range(i + 2, N):
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], cuts[j] - cuts[i] + dp[i][k] + dp[k][j])
        return dp[0][N - 1]


s = Solution()
print(s.minCost_TopDown(7, [1, 3, 4, 5]))
print(s.minCost_Dp(7, [1, 3, 4, 5]))
print(s.minCost_TopDown(9, [5, 6, 1, 4, 2]))
print(s.minCost_Dp(9, [5, 6, 1, 4, 2]))
print(s.minCost_TopDown(5709,
                        [5033, 3175, 655, 3763, 1378, 3633, 758, 3306, 2928, 4775, 218, 5052, 1867, 4458, 4548, 1275,
                         2965, 870, 5141, 2717, 1256, 3789, 612, 4351, 1331, 3923, 5371, 5637, 2834, 3445, 5409, 1600,
                         963, 5390, 3247, 2059, 5428, 3018, 3899, 5076, 1664, 629, 2119, 5302, 3416, 1685, 1097, 3292,
                         2145, 1186, 3188]))
print(s.minCost_Dp(5709,
                   [5033, 3175, 655, 3763, 1378, 3633, 758, 3306, 2928, 4775, 218, 5052, 1867, 4458, 4548, 1275, 2965,
                    870, 5141, 2717, 1256, 3789, 612, 4351, 1331, 3923, 5371, 5637, 2834, 3445, 5409, 1600, 963, 5390,
                    3247, 2059, 5428, 3018, 3899, 5076, 1664, 629, 2119, 5302, 3416, 1685, 1097, 3292, 2145, 1186,
                    3188]))
