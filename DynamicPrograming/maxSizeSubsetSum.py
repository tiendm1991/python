def maxSizeSubsetSum(arr, k):
    n = len(arr)
    dp = [[-1 for i in range(k+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 0
    for i in range(1, n+1):
        e = arr[i-1]
        for j in range(1, k+1):
            dp[i][j] = max(dp[i][j], dp[i-1][j])
            if j >= e and dp[i-1][j-e] != -1:
                dp[i][j] = max(dp[i][j], dp[i-1][j-e]+1)
    return dp[n][k]

print(maxSizeSubsetSum([2, 10, 3, 5, 7, 15], 10))
print(maxSizeSubsetSum([1, 2, 3, 4, 5], 11))

