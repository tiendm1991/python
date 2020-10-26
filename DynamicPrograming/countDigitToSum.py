def countDigitToSum(n, s):
    if n * 9 < s or s == 0:
        return 0
    dp = [[0 for i in range(s + 1)] for j in range(n + 1)]
    for i in range(1, s + 1):
        if i > 9:
            break
        dp[1][i] = 1
    for i in range(2, n + 1):
        for j in range(1, s + 1):
            for k in range(10):
                if j >= k:
                    dp[i][j] += dp[i - 1][j - k]
                else:
                    break
    return dp[n][s]


print(countDigitToSum(3, 6))
