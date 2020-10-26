from datetime import datetime


def longestValidParentheses(s):
    n = len(s)
    if n < 2:
        return 0
    dp = [0 for i in range(n)]
    dp[1] = 2 if s[0] == '(' and s[1] == ')' else 0
    for i in range(2, n):
        if s[i] == '(':
            continue
        if s[i - 1] == '(':
            dp[i] = dp[i - 2] + 2
        elif dp[i - 1] != 0:
            if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                dp[i] = dp[i - 1] + 2
                if i - dp[i - 1] - 2 >= 0:
                    dp[i] += dp[i - dp[i - 1] - 2]
    return max(dp)


start = datetime.now()
print(longestValidParentheses("(()))())("))
print(datetime.now() - start)
# 01234567890123
# (()))())(
