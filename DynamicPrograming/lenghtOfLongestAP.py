def lenghtOfLongestAP(arr):
    n = len(arr)
    arr.sort()
    dp = [2 for i in range(n + 1)]
    prev = [False for i in range(arr[-1] + 1)]
    dp[0] = 0
    dp[1] = 1
    prev[arr[0]], prev[arr[1]] = True, True
    for i in range(3, n + 1):
        x3 = arr[i - 1]
        prev[x3] = True
        for j in range(2, i):
            x2 = arr[j - 1]
            x1 = 2 * x2 - x3
            if prev[x1]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(dp)
    return max(dp)


print(lenghtOfLongestAP([2, 4, 6, 8, 10]))
print(lenghtOfLongestAP([1, 7, 10, 15, 27, 29]))
print(lenghtOfLongestAP([3, 7, 10, 14, 25, 27, 29]))
print(lenghtOfLongestAP([5, 10, 15, 20, 25, 30]))
print(lenghtOfLongestAP([1, 7, 10, 13, 14, 19]))
