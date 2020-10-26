def DivisionPossible(arr, k):
    s, ma, n = sum(arr), max(arr), len(arr)
    if s % k != 0:
        return False
    avg = s // k
    if ma > avg:
        return False
    subset = [0] * k
    return help(arr, subset, avg, 0)


def help(arr, subset, avg, idx):
    n = len(arr)
    k = len(subset)
    if idx == n:
        return True
    x = arr[idx]
    for i in range(k):
        if subset[i] + x <= avg:
            subset[i] += x
            if help(arr, subset, avg, idx + 1):
                return True
            subset[i] -= x
    return False


print(DivisionPossible([1, 1, 1, 2, 3, 4, 5, 3], 4))
print(DivisionPossible([2, 4, 1, 3, 2], 3))
print(DivisionPossible([2, 2, 2, 3], 3))
