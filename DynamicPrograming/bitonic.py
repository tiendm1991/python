def bitonic(arr):
    n = len(arr)
    dp1 = [1 for i in range(n+1)]
    dp1[0] = 0
    for i in range(1, n+1):
        for j in range(1, i):
            if arr[j-1] < arr[i-1]:
                dp1[i] = max(dp1[i], dp1[j] + 1)
    dp2 = [1 for i in range(n+1)]
    dp2[0] = 0
    for i in range(n, 0, -1):
        for j in range(i+1, n+1):
            if arr[j-1] < arr[i-1]:
                dp2[i] = max(dp2[i], dp2[j] + 1)
    print(dp1)
    print(dp2)
    return max([dp1[i] + dp2[i] for i in range(n+1)]) - 1
print(bitonic([1, 11, 2, 10, 4, 5, 2, 1]))
