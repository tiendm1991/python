def longestEvenLengSubstr(s):
    n = len(s)
    arr = [int(c) for c in s]
    dp = [[0 for i in range(n)] for j in range(n)]
    dp2 = [0 for i in range(n)]
    for i in range(n):
        for j in range(i, n):
            dp[i][j] = arr[j] + dp[i][j-1]
    for i in range(1, n):
        for j in range(i):
            if (i - j) % 2 == 0:
                continue
            mid = (i + j) // 2
            if dp[j][mid] == dp[mid+1][i]:
                dp2[i] = i - j + 1
                break
    return max(dp2)


print(longestEvenLengSubstr('1538023'))

