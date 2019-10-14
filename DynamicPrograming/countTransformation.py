def countTransformation(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    dp = [[0 for i in range(n1+1)] for j in range(n2+1)]
    for i in range(n1+1):
        dp[0][i] = 1
    for i in range(1, n2+1):
        c2 = s2[i-1]
        for j in range(i, n1+1):
            c1 = s1[j-1]
            dp[i][j] = dp[i][j-1]
            if c1 == c2:
                dp[i][j] += dp[i - 1][j - 1]
    return dp[n2][n1]

print(countTransformation('abcccdf', 'abccdf'))

