def countTripletSum(arr):
    n = len(arr)
    S, m = sum(arr), 1
    triplet = []
    while (m * m * m <= S):
        triplet.append(m * m * m)
        m += 1
    m = max(arr)
    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(m + 1):
        for j in range(n - 1, -1, -1):
            if i == arr[j]:
                dp[i][j] = dp[i][j + 1] + 1
            else:
                dp[i][j] = dp[i][j + 1]
    s = 0
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            x = arr[i] + arr[j]
            for k in (triplet):
                y = k - x
                if y >= 0 and y <= m:
                    s += dp[y][j + 1]
    return s


print(countTripletSum([2, 5, 1, 20, 6, 15, 17, 24, 19]))
