def countWaysToJump(arr):
    n = len(arr)
    dp = [0 if arr[i] != 0 else -1 for i in range(n)]
    if n == 1:
        return dp
    dp[-1] = 1
    for i in range(n-2, -1, -1):
        if dp[i] == -1:
            continue
        for j in range(i+1, min(i + arr[i] + 1, n)):
            if dp[j] != -1:
                dp[i] += dp[j]
        if dp[i] == 0:
            dp[i] = -1
    dp[-1] = 0
    return dp


print(countWaysToJump([1, 3, 5, 8, 9, 1, 0, 7, 6, 8, 9]))
# 52 52 28 16 8 -1 -1 4 2 1 0

