def pathCountRec(arr, k):
    r = len(arr)
    c = len(arr[0])
    dp = [[[0 for l in range(k + 1)] for j in range(c + 1)] for i in range(r + 1)]
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            dp[i][j][arr[i - 1][j - 1]] = 1
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            element = arr[i - 1][j - 1]
            for x in range(k + 1):
                dp[i][j][x] += dp[i][j - 1][x - element] + dp[i - 1][j][x - element] + dp[i][j - 1][x] + dp[i - 1][j][x]
    return dp[r][c][k]


print(pathCountRec([[1, 2, 3],
                    [4, 6, 5],
                    [3, 2, 1]], 12))
# 8
