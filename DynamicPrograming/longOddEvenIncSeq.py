def longOddEvenIncSeq(arr):
    n = len(arr)
    dp = [1] * (n)
    even = [False] * (n)
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and arr[i] % 2 != arr[j] % 2:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


print(longOddEvenIncSeq([1, 12, 2, 22, 5, 30, 31, 14, 17, 11]))
# 1 2 5 30 31

