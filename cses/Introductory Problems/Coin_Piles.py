def f(x, y):
	a = None
	if 2 * x - y < 0 or (2 * x - y) % 3 != 0:
		return False
	a = (2 * x - y) // 3
	b = x - 2 * a
	return b >= 0
# assume choose "a" time 2 coin of pile1, "b" time 2 coin of pile2
# 2a + b = x (1)
# 2b + a = y (2)
# 2 * (1) - (2) => 3a = 2x - y -> a = (2 * x - y) // 3
n = int(input())
for i in range(n):
	x, y = input().split(' ')
	x, y = int(x), int(y)
	print("YES" if f(x, y) or f(y, x) else "NO")
