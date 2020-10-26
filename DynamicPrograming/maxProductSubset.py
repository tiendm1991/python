def maxProductSubset(arr):
    n = len(arr)
    maxProduct = 0;
    maxPositive, minNegative = 1, 1
    for i in range(n):
        e = arr[i]
        if e == 0:
            maxPositive, minNegative = 1, 1
            continue
        elif e > 0:
            maxPositive *= e
            minNegative *= e
        else:
            tmp = maxPositive
            maxPositive = max(minNegative * e, 1)
            minNegative = tmp * e
        maxProduct = max(maxProduct, maxPositive)
    return maxProduct if maxProduct > 1 else 1 if sum(arr) > 0 else 0


print(maxProductSubset([-2, -3, 0, 4, -2, 3, -10, 2, 6, -10]))
print(maxProductSubset([-2, -3, 0, -2, -40]))
print(maxProductSubset([0, -4, 0, -2]))
