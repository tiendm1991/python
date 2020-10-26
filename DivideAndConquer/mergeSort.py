def mergeSort(a):
    n = len(a)
    if n == 1:
        return
    mid = n // 2
    a1 = a[:mid]
    a2 = a[mid:]
    mergeSort(a1)
    mergeSort(a2)
    merge(a, a1, a2)
    return a


def merge(a, a1, a2):
    i, j, k = 0, 0, 0
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            a[k] = a1[i]
            i += 1
        else:
            a[k] = a2[j]
            j += 1
        k += 1
    while i < len(a1):
        a[k] = a1[i]
        i += 1
        k += 1
    while j < len(a2):
        a[k] = a2[j]
        j += 1
        k += 1
    return


print(mergeSort([1, 3, 4, 2, 5]))
