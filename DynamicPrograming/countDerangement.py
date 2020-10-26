def countDerangement(n):
    dp = [0 for i in range(n + 1)]
    dp[2] = 1
    dp[3] = 2
    for i in range(4, n + 1):
        dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2])
    return dp[n]


print(countDerangement(4))

# Explain.
# Suppose have 4 person 1,2,3,4 and 4 hat 1 2 3 4
# Because person 1 can not get hat 1 => hat 1 must given to person 2 3 or 4 => n-1 * (recursive)
# Let person 2 get 1 => the same case with person 3 and 4
# Case 1: Person 1 get 2 => 1(2), 2(1), 3(? not 3), 4(? not 4) => f(n-2)
# Case 2: Person 1 not get 2 => 1(? not 2), 2(1), 3(? not 3), 4(? not 4) => f(n-1)
# Conclusion: f(n) = (n-1) * (f(n-2) + f(n-1))
