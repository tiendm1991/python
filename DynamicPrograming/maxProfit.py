def maxProfit(arr, k):
    n = len(arr)
    dp = [[0 for i in range(n)] for j in range(k+1)]
    for i in range(1, k+1):
        miIdx = (i-1)*2
        mi = arr[miIdx]
        for j in range(i * 2 - 1, n):
            x1 = dp[i-1][j]
            x2 = dp[i][j-1]
            x3 = max(arr[j] - mi, 0) + dp[i-1][miIdx-1]
            dp[i][j] = max(x1, x2, x3)
            #dp[i][j] = max(dp[i-1][j], dp[i][j-1], max(arr[j] - mi, 0) + dp[i-1][miIdx-1])
            if arr[j] < mi:
                mi = arr[j]
                miIdx = j
    return dp
print(maxProfit([12, 14, 17, 10, 14, 13, 12, 15], 3))
# 12-17 + 10-14 + 12-15 = 12
print(maxProfit([10, 22, 5, 75, 65, 80], 2))
print(maxProfit([100, 30, 15, 10, 8, 25, 80], 3))

