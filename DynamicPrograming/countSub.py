def countSub(s):
    n = len(s)
    a = [''] + [x for x in s]
    r, r2 = [''], ['']
    for c in a:
        r = r2[::]
        for x in r:
            if x + c not in r2:
                r2.append(x + c)
    return len(r2)


def countSub2(s):
    n = len(s)
    dp = [0 for i in range(n + 1)]
    dp[0] = 1
    last = {}
    for i in range(1, n + 1):
        c = s[i - 1]
        dp[i] = 2 * dp[i - 1]
        if c in last:
            idx = last[c]
            dp[i] -= dp[idx - 1]
        last[c] = i
    return dp[n]


print('countSub O(n^2) %d' % countSub("gfgfg"))
print('countSub2 O(n) %d' % countSub2("gfgfg"))
