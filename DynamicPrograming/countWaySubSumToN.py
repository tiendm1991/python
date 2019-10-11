def countWaySubSumToN(n):
    dp = [[0 for j in range(n+1)] for i in range(n+1)]
    for i in range(2, n+1):
        dp[i][1] = 1
        dp[i][i-1] = 1
        dp[i][i] = 1
    for i in range(3, n+1):
        for j in range(i-2, 1, -1):
            dp[i][j] += sum(dp[i-j][1:j+1])
    print(dp)
    return sum(dp[n][1:n])

print(countWaySubSumToN(6))

