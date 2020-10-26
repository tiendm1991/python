def minSubArr(a):
    n = len(a)
    minLocal, minGlobal = a[0], a[0]
    for i in range(1, n):
        minLocal += a[i]
        minLocal = min(minLocal, a[i])
        minGlobal = min(minLocal, minGlobal, a[i])
    return minGlobal


print(minSubArr([-8, 3, -4, -5, 20, -7, -1]))
print(minSubArr([5, 3, 7, 6, 2, 6]))
