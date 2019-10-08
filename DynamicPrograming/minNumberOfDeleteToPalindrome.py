def minNumberOfDeleteToPalindrome(s):
    n = len(s)
    maxPalinDrome = getMaxPalindrome(s)
    return n - maxPalinDrome


def getMaxPalindrome(s):
    n = len(s)
    dp = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            x,y = s[i], s[j]
            if s[i] != s[j]:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])
            else:
                dp[i][j] = dp[i+1][j-1] + 2
    return dp[0][n-1]


print(minNumberOfDeleteToPalindrome('geeksforgeeks'))

