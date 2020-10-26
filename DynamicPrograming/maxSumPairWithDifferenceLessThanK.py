def maxSumPairWithDifferenceLessThanK(arr, k):
    n = len(arr)
    arr.sort()
    dp = [0] * n
    dp[1] = arr[0] + arr[1] if arr[1] - arr[0] < k else 0
    for i in range(2, n):
        if arr[i] - arr[i - 1] >= k:
            dp[i] = dp[i - 1]
            continue
        dp[i] = max(dp[i - 2] + arr[i] + arr[i - 1], dp[i - 1])
    return dp


print(maxSumPairWithDifferenceLessThanK([5, 15, 10, 300], 12))
# 3, 5, 9, 10, 12, 15, 17
# 0 8 14
