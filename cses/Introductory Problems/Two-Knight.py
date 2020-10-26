n = int(input())
dp = [0] * (n + 1)
if n >= 3:
    dp[3] = 8
if n >= 4:
    dp[4] = 24
for i in range(5, n + 1):
    dp[i] = 8 * i + 8 * (i - 4) * (i - 4) - dp[i - 4]
for i in range(1, n + 1):
    x = i ** 2
    print(x * (x - 1) // 2 - dp[i])
# Explain
# total: total way to choose 2 cell from board (n * n) * (n * n - 1) // 2 (2Cn)
# check the board n-4 x n-4 at center
# each cell has 8 way => has 8 * (n-4) * (n-4)
# but duplicated when 2 cell in board n-4 x n-4 => has 8 * (n-4) * (n-4) - f(n-4)
# check the border, each border has 2 * (n-2) => has 4 * 2 * (n-2) = 8 * (n-2)
# at 2 border near board n-4 x n-4, each corner has 4 way => has 16 way
# => has 8 * (n-2) + 16 + 8 * (n-4) * (n-4) - f(n-4)
# => 8n + 8(n-4)(n-4) - f(n-4) => using dp
