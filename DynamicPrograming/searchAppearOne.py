def searchAppearOne(a):
    return help(a, 0, len(a) - 1)


def help(a, left, right):
    mid = (left + right + 1) // 2
    if a[mid] != a[mid - 1] and a[mid] != a[mid + 1]:
        return a[mid]
    if mid % 2 == 0:
        if a[mid] == a[mid - 1]:
            return help(a, left, mid)
        else:
            return help(a, mid, right)
    else:
        if a[mid] == a[mid - 1]:
            return help(a, mid + 1, right)
        else:
            return help(a, left, mid - 1)


print(searchAppearOne([1, 1, 3, 4, 4, 5, 5, 7, 7, 8, 8]))
print(searchAppearOne([1, 1, 3, 3, 4, 4, 5, 5, 7, 8, 8]))
print(searchAppearOne([1, 1, 2, 4, 4, 5, 5, 6, 6]))

