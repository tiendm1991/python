def deleteDigit(n):
    s = str(n)
    a = [int(x) for x in s]
    n = len(a)
    dp = [0 for i in range(n)]
    x = a[0]
    for i in range(1, n):
        dp[i] = max(dp[i - 1] * 10 + a[i], x)
        x = x * 10 + a[i]
    return dp[n - 1]


print(deleteDigit(152))
