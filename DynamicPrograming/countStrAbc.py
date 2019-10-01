def countStrAbc(n):
    dp = [[[0 for i in range(3)] for b in range(2)] for c in range(n + 1)]
    dp[1][0][0] = 1
    dp[1][1][0] = 1
    dp[1][0][1] = 1
    dp[2][0][0] = 1
    dp[2][0][1] = 2
    dp[2][0][2] = 1
    dp[2][1][0] = 2
    dp[2][1][1] = 2
    dp[2][1][2] = 0
    for i in range(3, n + 1):
        for b in range(2):
            for c in range(3):
                if b == 0 and c == 0:
                    dp[i][b][c] = 1
                elif b == 0 and c == 1:
                    dp[i][b][c] = dp[i-1][0][1] + dp[i-1][0][0]
                elif b == 0 and c == 2:
                    dp[i][b][c] = dp[i-1][0][2] + dp[i-1][0][1]
                elif b == 1 and c == 0:
                    dp[i][b][c] = dp[i-1][1][0] + dp[i-1][0][0]
                elif b == 1 and c == 1:
                    dp[i][b][c] = dp[i-1][1][1] + dp[i-1][0][1] + dp[i-1][1][0]
                else: # 1 2
                    dp[i][b][c] = dp[i-1][1][2] + dp[i-1][0][2] + dp[i-1][1][1]
    return sum([sum(i) for i in dp[n]])

print(countStrAbc(3))
# 19
# aaa aab aac aba abc aca acb acc baa
# bac bca bcc caa cab cac cba cbc cca ccb

