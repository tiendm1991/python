def f(x, y):
    m = max(x, y)
    _min, _max = (m - 1) ** 2 + 1, m ** 2
    if m % 2 == 0:
        if m == x:
            return _max - (y - 1)
        else:
            return _min + (x - 1)
    else:
        if m == x:
            return _min + (y - 1)
        else:
            return _max - (x - 1)


N = int(input())
for _ in range(N):
    x, y = input().split(' ')
    x = int(x)
    y = int(y)
    print(f(x, y))
