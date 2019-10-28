def quicksort(a):
    n = len(a)
    qSort(a, 0, n - 1)
    return a


def qSort(a, l, h):
    if l < h:
        p = partition(a, l, h)
        qSort(a, l, p - 1)
        qSort(a, p + 1, h)


def partition(a, low, high):
    pivot = a[high]
    mark, i = low - 1, low
    while i < high:
        if a[i] < pivot:
            mark += 1
            a[i], a[mark] = a[mark], a[i]
        i += 1
    mark += 1
    a[high], a[mark] = a[mark], a[high]
    return mark


print(quicksort([8, 2, 12, 3, 4, 9, 11, 10, 7]))
print(quicksort([1, 8, 9, 3, 4, 5, 7]))
print(quicksort([4, 8, 7, 3, 15, 18, 12, 6, 8, 9, 21, 25, 23]))

