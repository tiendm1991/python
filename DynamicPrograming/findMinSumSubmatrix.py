def findMinSumSubmatrix(arr):
    r = len(arr)
    c = len(arr[0])
    result = 99999
    for i in range(r):
        tmp = [0 for x in range(c)]
        for j in range(i, r):
            for k in range(c):
                tmp[k] += arr[j][k]
            minLocal, minGlobal = tmp[0], tmp[0]
            for k in range(1, c):
                minLocal += tmp[k]
                minLocal = min(minLocal, tmp[k])
                minGlobal = min(minLocal, minGlobal)
            result = min(result, minGlobal)
    return result


print(findMinSumSubmatrix([[1, 2, -1, -4, -20],
                           [-8, -3, 4, 2, 1],
                           [3, 8, 10, 1, 3],
                           [-4, -1, 1, 7, -6]]))
