def countDerangement(n):
    dp = [0 for i in range(n + 1)]
    dp[2] = 1
    dp[3] = 2
    for i in range(4, n + 1):
        dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2])
    return dp[n]


print(countDerangement(4))

