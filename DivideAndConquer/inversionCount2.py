def inversionCount2(a):
    n = len(a)
    return count2(a, 0, n - 1)


def count2(a, left, right):
    if left >= right:
        return 0
    c = 0
    mid = (left + right + 1) // 2
    c += count2(a, left, mid - 1)
    c += count2(a, mid, right)
    a1 = a[left: mid]
    a2 = a[mid: right + 1]
    c += merge(a, a1, a2, left)
    return c


def merge(a, a1, a2, start):
    c = 0
    i, j, k = 0, 0, start
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


print(inversionCount2([2, 4, 1, 3, 5]))
print(inversionCount2([1, 20, 6, 4, 5]))
