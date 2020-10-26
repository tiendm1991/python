def maxSumAtLeastKDistant(arr, k):
    n = len(arr)
    dp = [0 for i in range(n + 1)]
    for i in range(1, k + 2):
        dp[i] = max(dp[i], arr[i - 1])
    for i in range(k + 2, n + 1):
        dp[i] = arr[i - 1]
        for j in range(1, i - k):
            dp[i] = max(dp[i], dp[j] + arr[i - 1])
    return max(dp)


print(maxSumAtLeastKDistant([50, 70, 40, 50, 90, 70, 60, 40, 70, 50], 2))
