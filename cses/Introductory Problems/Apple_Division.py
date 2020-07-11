def f(n, a):
    s = sum(a)
    target = s // 2
    _set = {0}
    for x in a:
        tmp = set()
        for y in _set:
            tmp.add(x + y)
        _set |= tmp
    _min = s
    for x in _set:
        _min = min(_min, abs(2 * x - s))
        if _min == 0:
            break
    return _min


n = int(input())
a = [int(c) for c in input().split(' ')]
print(f(n, a))
