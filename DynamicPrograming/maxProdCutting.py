def maxProdCutting(n):
    dp = [0 for i in range(n+1)]
    dp[2] = 1
    dp[3] = 2
    for i in range(4, n+1):
        for j in range(2, i // 2 + 1):
            dp[i] = max(dp[i], dp[j] * dp[i-j], dp[j] * (i-j), j * dp[i-j], j * (i-j))
    return dp[n]

print(maxProdCutting(10))
# 1 0
# 2 1
# 3 2
# 4 4
# 5 6
# 6 9
# 7 12
# 8 18: 2 3 3
# 9 24: 2 3 4
# 10 36: 3 3 4
