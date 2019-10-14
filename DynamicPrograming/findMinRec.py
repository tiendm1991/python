def findMinRec(arr):
    n = len(arr)
    s = sum(arr)
    dp = [[False for i in range(s+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][0] = True
    for i in range(1, n+1):
        for j in range(1, s+1):
            dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
    for i in range(s//2, 0, -1):
        if dp[n][i] and dp[n][s-i]:
            return abs(2 * i - s)
    return -1

print(findMinRec([1, 6, 11, 5]))
print(findMinRec([1, 6, 11, 5, 4, 12]))

