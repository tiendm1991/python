def printShortestSuperSeq(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    dp = [[0 for i in range(n2+1)] for j in range(n1+1)]
    for i in range(n1+1):
        c1 = s1[i-1]
        for j in range(n2+1):
            c2 = s2[j-1]
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif c1 == c2:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j])
    i, j = n1, n2
    s = ''
    while i > 0 or j > 0:
        if s1[i-1] == s2[j-1]:
            s = s1[i-1] + s
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i-1][j] + 1:
            s = s1[i-1] + s
            i -= 1
        else:
            s = s2[j - 1] + s
            j -= 1
    return s


print(printShortestSuperSeq('AGGTAB', 'GXTXAYB'))
print(printShortestSuperSeq('HELLO', 'GEEK'))

