def minJumps(arr):
    n = len(arr)
    dp = [n] * n
    dp[0] = 1
    for i in range(1, n):
        for j in range(i):
            if (j + arr[j] >= i):
                dp[i] = min(dp[i], dp[j] + 1)
    return dp[n - 1] - 1


print(minJumps([1, 3, 6, 1, 0, 9]))
