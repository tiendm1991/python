def maximizeSum(arr):
    arr.sort()
    if len(arr) == 1:
        return 0
    if len(arr) == 2:
        return 2 * (arr[1] - arr[0])
    a = []
    i, j = 0, len(arr)-1
    while i < j:
        a.append(arr[i])
        a.append(arr[j])
        i += 1
        j -= 1
    if i == j:
        a.append(arr[i])
    s = 0
    for i in range(len(arr)-1):
        s += abs(a[i] - a[i+1])
    s += abs(a[0] - a[-1])
    return s

print(maximizeSum([4,19,14,9,7,3,6,15,13,14]))