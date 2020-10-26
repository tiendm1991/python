n = int(input())
s = n * (n + 1) // 2
if s % 2 == 1:
    print(0)
else:
    mod = 10 ** 9 + 7
    target = s // 2
    dp = [[1 if j == 0 else 0 for j in range(target + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            dp[i][j] = dp[i - 1][j]
            if j - i >= 0:
                dp[i][j] = (dp[i][j] + dp[i - 1][j - i]) % mod
    print(dp[n - 1][target])
