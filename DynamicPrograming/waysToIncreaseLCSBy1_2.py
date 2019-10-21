def waysToIncreaseLCSBy1_2(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    ch = 'abcdefghijklmnopqrstuvwxyz'
    x = 0
    dp1 = [[0 for i in range(n1 + 1)] for j in range(n2 + 1)]
    for i in range(1, n2 + 1):
        for j in range(1, n1 + 1):
            if s2[i - 1] == s1[j - 1]:
                dp1[i][j] = dp1[i - 1][j - 1] + 1
            else:
                dp1[i][j] = max(dp1[i - 1][j], dp1[i][j - 1])
    L = dp1[n2][n1]
    dp2 = [[0 for i in range(n1 + 1)] for j in range(n2 + 1)]
    for i in range(n2-1, -1, -1):
        for j in range(n1-1, -1, -1):
            if s2[i] == s1[j]:
                dp2[i][j] = dp2[i + 1][j + 1] + 1
            else:
                dp2[i][j] = max(dp2[i + 1][j], dp2[i][j + 1])
    for i in range(1, n2+1):
        for j in range(n1+1):
            x1 = dp1[i-1][j]
            x2 = dp2[i][j]
            if x1 + x2 == L:
                x += 1
    return x


print(waysToIncreaseLCSBy1_2('abab', 'abc'))

