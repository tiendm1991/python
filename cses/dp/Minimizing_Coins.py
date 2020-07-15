def f(a):
    dp = [s+1 for i in range(s+1)]
    dp[0] = 0
    for i in range(1, s+1):
        for x in a:
            if i >= x:
                dp[i] = min(dp[i], dp[i-x] + 1)
    return dp[s] if dp[s] < s+1 else -1



var = input().split(' ')
n, s = int(var[0]), int(var[1])
a = [int(c) for c in input().split()]
print(f(a))
