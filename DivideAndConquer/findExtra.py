def findExtra(a1, a2):
    return help(a1, 0, len(a1) - 1, a2, 0, len(a2) - 1)


def help(a1, l1, r1, a2, l2, r2):
    if l2 == r2:
        return r1
    m1 = (l1 + r1 + 1) // 2
    m2 = (l2 + r2 + 1) // 2
    if m1 == m2:
        if a1[m1] == a2[m2]:
            return help(a1, m1, r1, a2, m2, r2)
        else:
            return help(a1, l1, m1, a2, l2, m2-1)
    else:
        if a1[m1] == a2[m2]:
            return help(a1, l1, m1, a2, l2, m2)
        else:
            return help(a1, m1-1, r1, a2, m2, r2)


print(findExtra([2, 4, 6, 8, 9, 10, 12], [2, 4, 6, 8, 10, 12]))
print(findExtra([3, 5, 7, 9, 11, 13], [3, 5, 7, 11, 13]))
print(findExtra([2, 3, 4, 6, 8, 10, 12], [2, 4, 6, 8, 10, 12]))
print(findExtra([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 6]))
print(findExtra([1, 2, 3, 4, 5, 6], [1, 2, 3, 5, 6]))

