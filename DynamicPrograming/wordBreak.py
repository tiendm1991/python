d = {'i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice', 'cream', 'icecream', 'mango', 'and'}


def wordBreak(s):
    n = len(s)
    dp = [False for i in range(n + 1)]
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            x = s[j:i]
            if x not in d:
                dp[i] = False
            else:
                dp[i] = dp[j]
                if dp[j]:
                    break
    print(dp)
    return dp[n]


print(wordBreak('samsungandmango'))
