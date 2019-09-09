def findPartion(arr):
    n = len(arr)
    s = sum(arr)
    if s % 2 != 0:
        return False
    x = s//2
    dp = [[False for i in range(n + 1)] for j in range(x+1)]
    # dp[i][j]: sum of 'j' element == 'i' -> True or False
    for i in range(n+1):
        dp[0][i] = True
    for i in range(1, x+1):
        for j in range(1, n+1):
            if dp[i][j-1]:
                dp[i][j] = True
            elif arr[j-1] <= i:
                dp[i][j] = dp[i-arr[j-1]][j-1]
    return dp[x][n]

print(findPartion([3, 1, 2, 7, 2, 1]))
