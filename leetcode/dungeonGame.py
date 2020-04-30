def dungeonGame(a):
    m = len(a)
    n = len(a[0])
    dp = [[0 for i in range(n)] for j in range(m)]
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if i == m-1 and j == n-1:
                dp[m-1][n-1] = 1
                continue
            if j + 1 < n:
                dp[i][j] = 1 + max(dp[i][j+1] - a[i][j+1]-1, 0)
            if i + 1 < m:
                if dp[i][j] == 0:
                    dp[i][j] = 1 + max(dp[i+1][j] - a[i+1][j]-1, 0)
                else:
                    dp[i][j] = min(dp[i][j], 1 + max(dp[i+1][j] - a[i+1][j]-1, 0))
    return 1 + max(dp[0][0] - a[0][0] - 1, 0)

print(dungeonGame(
[[1, -2, 3],
 [2, -2, -2]]))