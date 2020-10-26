def f(n):
    mod = 10 ** 9 + 7
    a = [1, 2, 3, 4, 5, 6]
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for x in a:
            if i >= x:
                dp[i] = (dp[i] + dp[i - x]) % mod
    return dp[n]


n = int(input())
print(f(n))
