def countNonDecreasing(n):
    dp = [[0 for i in range(10)] for j in range(n + 1)]
    for i in range(10):
        dp[1][i] = 1
    for i in range(2, n + 1):
        for j in range(1, 10):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
    return sum([sum(dp[i]) for i in range(n + 1)])


print(countNonDecreasing(3))
