def kth(a1, a2, k):
    return help(a1, 0, len(a1) - 1, a2, 0, len(a2) - 1, k)


def help(a1, l1, r1, a2, l2, r2, k):
    if r1 - l1 + r2 - l2 + 2 < k:
        return -1
    if k == 1:
        return min(a1[l1], a2[l2])
    elif r1 - l1 + r2 - l2 + 2 == k:
        return max(a1[r1], a2[r2])
    elif l1 > r1:
        return a2[k-1]
    elif l2 > r2:
        return a1[k-1]

    i = min(r1 - l1 + 1, k // 2)
    j = min(r2 - l2 + 1, k // 2)
    if a1[l1 + i - 1] > a2[l2 + j - 1]:
        return help(a1, l1, r1, a2, l2 + j, r2, k - j)
    else:
        return help(a1, l1 + i, r1, a2, l2, r2, k - i)


print(kth([1, 3, 4, 9], [2, 6, 7, 8], 5))
print(kth([6, 7, 10], [8, 9], 3))
print(kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 7))
# 1 2 3 4 6 7 8 9 10

