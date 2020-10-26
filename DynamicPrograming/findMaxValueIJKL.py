def findMaxValueIJKL(arr):
    n = len(arr)
    dp1 = [0 for i in range(n)]
    dp2 = [0 for i in range(n)]
    mi = arr[0]
    for i in range(1, n - 2):
        dp1[i] = max(dp1[i - 1], arr[i] - mi)
        if arr[i] < mi:
            mi = arr[i]
    ma = arr[n - 1]
    for i in range(n - 2, 1, -1):
        dp2[i] = max(dp2[i + 1], ma - arr[i])
        if arr[i] > ma:
            ma = arr[i]
    result = 0
    for i in range(1, n - 2):
        result = max(result, dp1[i] + dp2[i + 1])
    return result


print(findMaxValueIJKL([4, 5, 1, 9, 8, 2, 20]))
print(findMaxValueIJKL([4, 8, 9, 2, 20]))
# Maximize arr[j] – arr[i] + arr[l] – arr[k], such that i < j < k < l.
# Find the maximum value of arr[j] – arr[i] + arr[l] – arr[k], such that i < j < k < l
