def maxCost(m):
    n = len(m)
    dp = [[0 for i in range(n)] for j in range(n)]
    dp[0][0] = m[0][0]
    for i in range(1,n):
        for j in range(n):
            x1 = dp[i-1][j] + m[i][j] if dp[i-1][j] > 0 else 0
            x2 = dp[i-1][j-1] + m[i][j] if j > 0 and dp[i-1][j-1] > 0 else 0
            dp[i][j] = max(x1,x2)
    print(dp)
    return max(dp[n-1])
print(maxCost([ [4, 1, 5, 6, 1],
                [2, 9, 2, 11, 10],
                [15, 1, 3, 15, 2],
                [16, 92, 41,4, 3],
                [8, 142, 6, 4, 8]]))
