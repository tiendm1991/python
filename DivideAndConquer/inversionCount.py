def inversionCount(a):
    c = 0
    n = len(a)
    if n == 1:
        return 0
    mid = n // 2
    a1 = a[:mid]
    a2 = a[mid:]
    c += inversionCount(a1)
    c += inversionCount(a2)
    c += merge(a, a1, a2)
    return c


def merge(a, a1, a2):
    c = 0
    i, j, k = 0, 0, 0
    n1, n2 = len(a1), len(a2)
    while i < n1 and j < n2:
        if a1[i] < a2[j]:
            a[k] = a1[i]
            i += 1
        else:
            a[k] = a2[j]
            j += 1
            c += n1 - i
        k += 1
    while i < n1:
        a[k] = a1[i]
        i += 1
        k += 1
    while j < n2:
        a[k] = a2[j]
        j += 1
        k += 1
    return c


print(inversionCount([2, 4, 1, 3, 5]))
print(inversionCount([1, 20, 6, 4, 5]))
