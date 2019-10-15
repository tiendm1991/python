def minPalPartion(s):
    n = len(s)
    dp = [i for i in range(n+1)]
    if s[0] == s[1]:
        dp[2] = 1
    for i in range(3, n+1):
        for j in range(i):
            if isPalindrome(s, j-1, i-1):
                dp[i] = min(dp[i], dp[j-1] + 1)
    return dp[n]-1
def isPalindrome(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
print(minPalPartion('ababbbabbababa'))
# a|babbbab|b|ababa
