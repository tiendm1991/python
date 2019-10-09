def isSubSeqDivisible8(s):
    arr = [int(x) for x in s]
    n = len(arr)
    dp = [[False for j in range(8)] for i in range(n+1)]
    dp[1][arr[0]%8] = True
    for i in range(2, n+1):
        x = arr[i-1]
        dp[i][x % 8] = True
        for j in range(8):
            if dp[i-1][j]:
                dp[i][j] = True
                dp[i][(j * 10 + x) % 8] = True
    return dp[n][0]


print(isSubSeqDivisible8('1787075866'))
print(isSubSeqDivisible8('6673177113'))
print(isSubSeqDivisible8('3144'))
# dp[i][j] : from i element first, True have number % 8 == j
# For all mod of 8 from dp[i-1], if have mod is j => dp[i] has mod is 10 * mod + arr[i] % 8 => dp[i][(j * 10 + x) % 8] = True
