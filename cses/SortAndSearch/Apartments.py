def f(x, b, k):
    x.sort()
    b.sort()
    ans = 0
    i = 0
    for a in x:
        while i < m and b[i] + k < a:
            i += 1
        if i < m and b[i] - k <= a:
            ans += 1
            i += 1
    return ans


n, m, k = input().split(' ')
n, m, k = int(n), int(m), int(k)
x = [int(c) for c in input().split(' ')]
b = [int(c) for c in input().split(' ')]
print(f(x, b, k))
