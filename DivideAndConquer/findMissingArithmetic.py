def findMissingArithmetic(a):
    return findMissing(a, 0, len(a)-1)


def findMissing(a, left, right):
    if right - left == 2:
        if a[left + 1] - a[left] < a[right] - a[left + 1]:
            return (a[right] + a[left+1]) // 2
        else:
            return (a[left] + a[left+1]) // 2
    n = right - left + 1
    u = (a[right] - a[left]) // n
    mid = (right + left + 1) // 2
    nLeft = mid - left + 1
    if nLeft * u == a[mid] - a[left]:
        return findMissing(a, left, mid)
    else:
        return findMissing(a, mid-1, right)

print(findMissingArithmetic([1, 6, 11, 16, 21, 31]))
print(findMissingArithmetic([2, 4, 8, 10, 12, 14]))
