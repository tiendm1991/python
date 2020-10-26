def largestSubsetDivisible(arr):
    arr.sort()
    n = len(arr)
    dp = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        dp[i] = 1
        for j in range(1, i):
            if arr[i - 1] % arr[j - 1] == 0:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp[n]


# print(largestSubset([18, 1, 3, 6, 13, 17]))
print(largestSubsetDivisible([10, 5, 3, 15, 6, 20]))
# 3, 5, 10, 15, 20
