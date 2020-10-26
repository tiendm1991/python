def minRemovalTo2MinMoreThanMax(arr):
    arr.sort()
    n = len(arr)
    dp = [1 for i in range(n)]
    for i in range(1, n):
        for j in range(i):
            if arr[i] < 2 * arr[j]:
                dp[i] = i - j + 1
                break
    return n - max(dp)


print(minRemovalTo2MinMoreThanMax([4, 5, 9, 10, 11, 12, 15, 100, 200]))
# 4, 5, 9, 10, 11, 12, 15, 100, 200
