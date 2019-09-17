def maxAlternateSum(arr):
    n = len(arr)
    head = arr[0]
    dp = [0 for i in range(n)]
    decrease = [True for i in range(n)]
    dp[0] = arr[0]
    for i in range(1, n):
        x = arr[i]
        for j in range(i):
            if decrease[j] and arr[j] > x:
                dp[i] = max(dp[i], dp[j] + x)
                decrease[i] = False
            elif not decrease[j] and arr[j] < x:
                dp[i] = max(dp[i], dp[j] + x)
                decrease[i] = True
    print(dp)
    return dp[n-1]
print(maxAlternateSum([9, 4, 7, 6, 5, 3, 8]))
# 9 4 7 6 8 = 34

