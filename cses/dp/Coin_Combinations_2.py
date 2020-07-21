def f2(n, s):
    mod = 10 ** 9 + 7
    dp = [[1 if i == 0 else 0 for j in range(n + 1)] for i in range(s + 1)]
    for i in range(1, s + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i][j - 1]
            if i >= a[j - 1]:
                dp[i][j] = (dp[i][j] + dp[i - a[j - 1]][j]) % mod
    return dp[s][n]


def f(n, s):
    mod = 10 ** 9 + 7
    dp = [0 for i in range(s + 1)]
    dp[0] = 1
    for i in range(n):
        for j in range(1, s + 1):
            if j >= a[i]:
                dp[j] = (dp[j] + dp[j - a[i]]) % mod
    return dp[s]


var = input().split(' ')
n, s = int(var[0]), int(var[1])
a = [int(c) for c in input().split(' ')]
print(f(n, s))
