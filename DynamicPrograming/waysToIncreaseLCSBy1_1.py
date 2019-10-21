def waysToIncreaseLCSBy1_1(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    ch = 'abcdefghijklmnopqrstuvwxyz'
    l = lcs(s1,s2)
    x = 0
    for c in ch:
        if c not in s2:
            continue
        for i in range(n1+1):
            s1New = s1[0:i] + c + s1[i:n1]
            if lcs(s1New, s2) == l+1:
                x += 1
    return x

def lcs(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    dp = [[0 for i in range(n1 + 1)] for j in range(n2 + 1)]
    for i in range(1, n2 + 1):
        for j in range(1, n1 + 1):
            if s2[i - 1] == s1[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n2][n1]


print(waysToIncreaseLCSBy1_1('abcabc', 'abcd'))

