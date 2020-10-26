def maxDotProductTwoArray(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    dp = [[0 for i in range(n1 + 1)] for j in range(n2 + 1)]
    for i in range(1, n2 + 1):
        for j in range(i, n1 + 1):
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 1] + arr2[i - 1] * arr1[j - 1])
    return dp


print(maxDotProductTwoArray([2, 3, 1, 7, 8], [3, 6, 7]))
# 3 6 7
# 2 3 1 7 8
# sample: 3 6 -> 2 3 1 7.
# If arr2 get 6 -> convert problem to 3 -> 2 3 1 + 6 * 7
# else -> convert problem to 3 6 -> 2 3 1
