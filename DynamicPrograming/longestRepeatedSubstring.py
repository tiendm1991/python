def longestRepeatedSubstring(s):
    n = len(s)
    dp = [[0 for j in range(n + 1)] for j in range(n + 1)]
    for i in range(1, n):
        c1 = s[i - 1]
        for j in range(i + 1, n + 1):
            c2 = s[j - 1]
            if c2 == c1:
                if j - dp[i - 1][j - 1] > i:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = dp[i - 1][j - 1]
    idx, m = 0, 0
    for i in range(1, n + 1):
        x = max(dp[i])
        if x > m:
            m = x
            idx = i
    return s[idx - m:idx]


print(longestRepeatedSubstring('aabaaba'))
# aabaaba
# 012345678
