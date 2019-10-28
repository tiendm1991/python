def mergeSort2(a):
    n = len(a)
    sort(a, 0, n - 1)
    return a


def sort(a, left, right):
    if left >= right:
        return
    mid = (left + right + 1) // 2
    sort(a, left, mid - 1)
    sort(a, mid, right)
    a1 = a[left: mid]
    a2 = a[mid: right + 1]
    merge(a, a1, a2, left)


def merge(a, a1, a2, start):
    i, j, k = 0, 0, start
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


print(mergeSort2([1, 3, 4, 2, 5]))

