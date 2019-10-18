def minSizeRec(arr, k):
    n = len(arr)
    mi = n
    if n < 3:
        return n
    for i in range(n-2):
        if arr[i+1] - arr[i] == k and arr[i+2] - arr[i+1] == k:
            newArr = arr[:i]
            if i + 3 < n:
                newArr += arr[(i+3):]
            mi = min(mi, minSizeRec(newArr, k))
    return mi

print(minSizeRec([6, 2, 3, 4, 5, 6, 4, 2], 1))



