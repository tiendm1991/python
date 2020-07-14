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

def f2(x, n):
    if n < 5:
        return(x ** n) % mod
    ans = 1
    m = x
    while n > 1:
        if n % 2 == 1:
            ans = (ans * m) % mod
        m = (m * m) % mod
        x = (x * x) % mod
        n //= 2
    return (ans * x) % mod
# explain
# assume calculate x^27
# => calculate (((x^2.x)^2)^2.x)^2.x
# => calculate x^16.(x^1.x^2.x^8)
# => from 2 to n, each time n //= 2 -> x = x^2 => calculate x^16
# => m = x^1.x^2.x^8
# => ok

mod = 10 ** 9 + 7
t = int(input())
for _ in range(t):
    var = input().split(' ')
    print(f(int(var[0]) % mod, int(var[1])))
