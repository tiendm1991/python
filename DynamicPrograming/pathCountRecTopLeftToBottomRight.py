def pathCountRecTopLeftToBottomRight(arr, k):
    r = len(arr)
    c = len(arr[0])
    dp = [[[0 for l in range(k+1)] for j in range(c+1)] for i in range(r+1)]
    dp[1][1][arr[0][0]] = 1
    for i in range(1, r+1):
        for j in range(1, c+1):
            element = arr[i - 1][j - 1]
            for x in range(k+1):
                if x >= element:
                    dp[i][j][x] += dp[i][j-1][x - element] + dp[i-1][j][x-element]
    return dp[r][c][k]

print(pathCountRecTopLeftToBottomRight([[1, 2, 3],
                                       [4, 6, 5],
                                       [3, 2, 1]], 12))
# 1 -> 2 -> 6 -> 2 -> 1
# 1 -> 2 -> 3 -> 5 -> 1

