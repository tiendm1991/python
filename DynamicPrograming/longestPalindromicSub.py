def longestPalindromicSub(s):
    n = len(s)
    dp = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for i in range(n - 1, -1, -1):
        x = s[i]
        for j in range(i + 1, n):
            y = s[j]
            if x == y and i != j:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
    return dp[0][n - 1]


print(longestPalindromicSub('GEEKSFORGEEKS'))
# GEEKSFORGEEKS
# 0123456789012
