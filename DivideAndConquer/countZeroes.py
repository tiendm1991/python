def countZeroes(a):
    x = firstZero(a, 0, len(a)-1)
    return len(a) - x


def firstZero(a, left, right):
    if a[right] == 1:
        return -1
    if right - left == 1:
        return right
    mid = (left + right + 1) // 2
    if a[mid] == 0:
        return firstZero(a, left, mid)
    else:
        return firstZero(a, mid, right)


print(countZeroes([1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]))
