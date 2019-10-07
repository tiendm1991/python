def minimumSquare(a, b):
    n = min(a,b)
    m = max(a,b)
    dp = [[99 for i in range(m+1)] for j in range(n+1)]
    for i in range(1, n+1):
        dp[i][i] = 1
    for j in range(1, m+1):
        dp[1][j] = j
        dp[0][j] = 0
    for i in range(2, n+1):
        for j in range(i+1, m+1):
            for k in range(1, i//2+1):
                dp[i][j] = min(dp[i][j], dp[k][j] + dp[i-k][j])
            dp[i][j] = min(dp[i][j], (j//i) + dp[j%i][i])
    return dp[n][m]


print(minimumSquare(4,5))
print(minimumSquare(30,36))

