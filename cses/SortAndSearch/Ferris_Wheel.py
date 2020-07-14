def f(a):
    a.sort()
    ans = n
    i, j = 0, n - 1
    while i < j:
        if a[i] + a[j] <= w:
            ans -= 1
            i += 1
        j -= 1
    return ans


var = input().split(' ')
n, w = int(var[0]), int(var[1])
a = [int(c) for c in input().split()]
print(f(a))
