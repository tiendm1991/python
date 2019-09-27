def countIncreaseSub(arr):
    n = len(arr)
    dp = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        dp[i] = 1
        for j in range(1, i):
            if arr[i - 1] > arr[j - 1]:
                dp[i] += dp[j]
    return sum(dp)


#print(countIncreaseSub([3, 2, 4, 5, 4]))
# 14
print(countIncreaseSub([1, 2, 3, 4]))
# 15

