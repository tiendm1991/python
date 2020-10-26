def countWaysPQR(p, q, r):
    s = p + q + r
    dp = [[[[0 for x in range(3)] for i in range(q + 1)] for j in range(p + 1)] for k in range(s + 1)]
    dp[1][0][0][2] = 1
    dp[1][1][0][0] = 1
    dp[1][0][1][1] = 1
    for i in range(2, s + 1):
        for p1 in range(min(i + 1, p + 1)):
            for q1 in range(min(i + 1, q + 1)):
                r1 = i - (p1 + q1)
                if r1 < 0:
                    break
                if r1 == i:
                    continue
                if r1 == 0:
                    if q1 > 0 and p1 > 0:
                        if p1 == q1:
                            dp[i][p1][q1][0] = 1
                            dp[i][p1][q1][1] = 1
                        elif p1 - q1 == 1:
                            dp[i][p1][q1][0] = 1
                        elif q1 - p1 == 1:
                            dp[i][p1][q1][1] = 1
                else:
                    if p1 == 0 or q1 == 0:
                        if p1 == r1:
                            dp[i][p1][q1][0] = 1
                            dp[i][p1][q1][2] = 1
                        elif q1 == r1:
                            dp[i][p1][q1][1] = 1
                            dp[i][p1][q1][2] = 1
                        elif q1 - r1 == 1:
                            dp[i][p1][q1][1] = 1
                        elif p1 - r1 == 1:
                            dp[i][p1][q1][0] = 1
                        elif r1 - p1 == 1 or r1 - q1 == 1:
                            dp[i][p1][q1][2] = 1
                    else:
                        dp[i][p1][q1][2] = dp[i - 1][p1][q1][0] + dp[i - 1][p1][q1][1]
                        dp[i][p1][q1][1] = dp[i - 1][p1][q1 - 1][0] + dp[i - 1][p1][q1 - 1][2]
                        dp[i][p1][q1][0] = dp[i - 1][p1 - 1][q1][1] + dp[i - 1][p1 - 1][q1][2]

    return sum(dp[s][p][q])


print(countWaysPQR(2, 1, 1))
