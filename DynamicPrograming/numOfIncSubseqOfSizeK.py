def numOfIncSubseqOfSizeK(arr, k):
    n = len(arr)
    if k == 1:
        return n
    dp = [[0 for i in range(n+1)] for j in range(k+1)]
    for a in range(1, k+1):
        for i in range(1, n+1):
            if a == 1:
                dp[a][i] = 1
            elif i >= a:
                for j in range(1, i):
                    if arr[j-1] < arr[i-1]:
                        dp[a][i] += dp[a-1][j]
    return sum(dp[k])


print(numOfIncSubseqOfSizeK([2, 6, 4, 5, 7], 3))
# 1 2 2 3 4
# 0 0 0 0 0 0
# 0 1 1 1 1 1
# 0 0 1 1 2 4
# 0 0 0 0 1 4
print(numOfIncSubseqOfSizeK([12, 8, 11, 13, 10, 15, 14, 16, 20], 4))
# 39
