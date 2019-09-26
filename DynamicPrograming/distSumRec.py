def distSumRec(arr):
    n = len(arr)
    s = sum(arr)
    dp = [[False for i in range(s+1)] for j in range(n+1)]
    dp[0][0] = True
    for i in range(1, n+1):
        element = arr[i-1]
        for x in range(s+1):
            if dp[i-1][x]:
                dp[i][x] = True
            elif x >= element:
                dp[i][x] = dp[i-1][x - element]
    result = []
    for i in range(s+1):
        if dp[n][i]:
            result.append(i)
    return result

print(distSumRec([2, 3, 5]))
# [0, 2, 3, 5, 7, 8, 10]

