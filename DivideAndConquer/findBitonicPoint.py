def findBitonicPoint(a):
    return find(a, 0, len(a) - 1)


def find(a, left, right):
    if a[left] > a[left+1]:
        return a[left]
    elif a[right] > a[right-1]:
        return a[right]
    mid = (left + right + 1) // 2
    if a[mid] > a[mid-1]:
        return find(a, mid, right)
    else:
        return find(a, left, mid-1)


print(findBitonicPoint([6, 7, 8, 11, 9, 5, 2, 1]))
print(findBitonicPoint([6, 7, 8, 5, 4, 3, 2, 1]))


