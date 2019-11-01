def getMedianOfTwoArraySorted(a1, a2):
    return help(a1, 0, len(a1) - 1, a2, 0, len(a2) - 1)


def help(a1, l1, r1, a2, l2, r2):
    if r1 - l1 <= 1 and r2 - l2 <= 1:
        return float((max(a1[l1], a2[l2]) + min(a1[r1], a2[r2]))) / 2
    m1 = (l1 + r1 + 1) // 2
    m2 = (l2 + r2 + 1) // 2
    if a1[m1] < a2[m2]:
        x = min(m1 - l1, r2 - m2)
        return help(a1, l1 + x, r1, a2, l2, r2 - x)
    else:
        x = min(r1 - m1, m2 - l2)
        return help(a1, l1, r1 - x, a2, l2 + x, r2)


print(getMedianOfTwoArraySorted([1, 2, 3, 8], [4, 5, 7, 10]))
# 1 2 3 4 5 7 8 10
print(getMedianOfTwoArraySorted([2, 13, 17, 30, 45], [1, 12, 15, 26, 38]))
# 1 2 12 13 15 17 26 30 38 45

