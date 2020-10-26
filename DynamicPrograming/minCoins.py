def minCoins(arr, v):
    n = len(arr)
    dp = [[n + 1 for i in range(v + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 0
    for i in range(1, n + 1):
        x = arr[i - 1]
        if x == v:
            return 1
        for j in range(1, v + 1):
            dp[i][j] = min(dp[i][j], dp[i - 1][j])
            if j >= x and dp[i - 1][j - x] != n + 1:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - x] + 1)
    return dp[n][v] if dp[n][v] <= n else -1


print(minCoins([25, 10, 5], 30))
# 25, 5
print(minCoins([8, 5, 4, 2, 6], 11))
# 5, 6
