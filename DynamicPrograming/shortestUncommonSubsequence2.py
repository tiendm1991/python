def shortestUncommonSubsequence(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    dp = [[-1 for i in range(n2 + 1)] for j in range(n1 + 1)]
    for i in range(1, n1 + 1):
        dp[i][0] = 1
    for i in range(1, n1 + 1):
        x = s1[i - 1]
        for j in range(1, n2 + 1):
            if dp[i][j - 1] == -1:
                dp[i][j] = -1
            elif dp[i - 1][j] != -1:
                dp[i][j] = dp[i - 1][j]
            elif dp[i - 1][j - 1] == -1 and s2[j - 1] == x:
                dp[i][j] = -1
            else:
                k = j - 1
                while k > 0:
                    if s2[k - 1] == x:
                        break
                    k -= 1
                if k == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][k - 1] + 1
    print(dp)
    return dp[n1][n2]


print(shortestUncommonSubsequence("babab", "acacbba"))
# babab bcacbba
