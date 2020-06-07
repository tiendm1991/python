class Solution:
    def minCost(self, houses, cost, m: int, n: int, target: int) -> int:
        MAX_VALUE = 10 ** 9
        # dp[i][k][j] is cost to painting i house with k neighborhoods and house[i-1] has color j
        dp = [[[0 if i == 0 and k == 0 else MAX_VALUE for j in range(n + 1)]
               for k in range(target + 1)]
              for i in range(m + 1)]
        for i in range(1, m + 1):
            for k in range(1, min(i, target) + 1):
                for j in range(1, n + 1):
                    if houses[i - 1] != 0 and j != houses[i - 1]:
                        # check house[i-1] has been painted already => house[i-1] is only painted with color j
                        continue
                    c = cost[i - 1][j - 1] if houses[i - 1] == 0 else 0
                    dp[i][k][j] = dp[i - 1][k][j] + c
                    for x in range(1, n + 1):
                        if (i > 1 and houses[i - 2] != 0 and x != houses[i - 2]) or x == j:
                            # check if previous house has color != j
                            continue
                        dp[i][k][j] = min(dp[i][k][j], dp[i - 1][k - 1][x] + c)
        result = min(dp[m][target])
        return result if result < MAX_VALUE else -1


s = Solution()
print(s.minCost([0, 0, 0, 0, 0], [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], 5, 2, 3))
print(s.minCost([0, 0, 2, 3], [[5, 4, 1], [1, 2, 1], [4, 4, 2], [5, 2, 5]], 4, 3, 4))
print(s.minCost([0, 2, 1, 2, 0], [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], 5, 2, 3))
