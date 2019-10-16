def sumZeroMatrix(arr):
    R = len(arr)
    C = len(arr[0])
    mGlobal = 0
    for i in range(R):
        tmp = [0 for x in range(C)]
        for j in range(i, R):
            l = j - i + 1
            for k in range(C):
                tmp[k] += arr[j][k]
            #print(tmp)
            w = getMaxWidth(tmp)
            mGlobal = max(mGlobal, l * w)
    return mGlobal


def getMaxWidth(arr):
    n = len(arr)
    w = 0
    s = arr[0]
    d = {arr[0]: 0}
    for i in range(1, n):
        x = arr[i]
        s += x
        if s == 0:
            w = max(w, i+1)
        elif s in d:
            w = max(w, i - d[s])
            continue
        d[s] = i

    return w


print(getMaxWidth([9, 2, 3, -1, -5, 0, -1, 2, 7]))
print(getMaxWidth([1,0,0,0,-1, 2]))
print(sumZeroMatrix([[9, 7, 16, 5],
                     [1, -6, -7, 3],
                     [1, 8, 7, 9],
                     [7, -2, 0, 10]]))

