n = int(input())
dp = [0] * (n+1)
if n >= 3:
	dp[3] = 8
if n >= 4:
	dp[4] = 24
for i in range(5, n+1):
	dp[i] = 8 * i + 8 * (i-4) * (i-4) - dp[i-4]
for i in range(1, n+1):
	x = i ** 2
	print(x * (x-1) // 2 - dp[i])