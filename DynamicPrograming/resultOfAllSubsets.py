def resultOfAllSubsets(arr):
    s = sum(arr)
    result = s
    n = len(arr)
    for i in range(2, n + 1):
        subSum = commbineKN(i - 1, n - 1) * s
        result += float(subSum) / i
    return result


def commbineKN(k, n):
    dp = [[0 for i in range(n + 1)] for j in range(k + 1)]
    for i in range(1, n + 1):
        dp[1][i] = i
    for i in range(2, k + 1):
        for j in range(i, n + 1):
            if i == j:
                dp[i][j] = 1
            elif i == j - 1:
                dp[i][j] = j
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
    return dp[k][n]


print(commbineKN(2, 4))
print(resultOfAllSubsets([2, 3, 5]))
print(resultOfAllSubsets([2, 3, 5, 7]))
# 1 2 3 4 5
# 1
# 12, 13, 14, 15: 1, n-1
# 123, 124, 125, 134, 135, 145: 2, n-1
# 1234, 1235, 1345: 3, n-1
# 12345: 4, n-1
