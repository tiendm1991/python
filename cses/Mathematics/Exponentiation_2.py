def f(x, n, m):
    if n < 2:
        return (x ** n) % m
    ans = 1
    # m = x
    while n > 1:
        if n % 2 == 1:
            ans = (ans * x) % m
        # m = (m * m) % mod
        x = (x * x) % m
        n //= 2
    return (ans * x) % m


mod = 10 ** 9 + 7
t = int(input())
for _ in range(t):
    var = input().split(' ')
    a = int(var[0]) % mod
    b = int(var[1]) % mod
    c = int(var[2]) % mod
    print(f(a, f(b, c, mod-1), mod))
