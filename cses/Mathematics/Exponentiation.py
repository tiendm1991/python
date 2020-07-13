def f(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    ans = 1
    while n > 0:
        if n % 2 != 0:
            ans = (ans * x) % mod
        x = (x ** 2) % mod
        n //= 2
    return ans


mod = 10**9 + 7
t = int(input())
for _ in range(t):
    var = input().split(' ')
    a, b = int(var[0]) % mod, int(var[1])
    print(f(a, b))