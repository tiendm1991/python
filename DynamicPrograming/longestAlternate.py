def longestAlternate(arr):
    n = len(arr)
    dp = help(arr, True)
    dp2 = help(arr, False)
    return max(dp[n - 1], dp2[n - 1])


def help(arr, decrease):
    n = len(arr)
    dp = [0 for i in range(n)]
    decrease = [True for i in range(n)] if decrease else [False for i in range(n)]
    dp[0] = 1
    for i in range(1, n):
        x = arr[i]
        for j in range(i):
            if decrease[j] and arr[j] > x and dp[j] != 0:
                dp[i] = max(dp[i], dp[j] + 1)
                decrease[i] = False
            elif not decrease[j] and arr[j] < x and dp[j] != 0:
                dp[i] = max(dp[i], dp[j] + 1)
                decrease[i] = True
    print(dp)
    return dp


print(longestAlternate([9, 4, 7, 6, 5, 3, 8]))
print(longestAlternate([10, 22, 9, 33, 31, 60]))
