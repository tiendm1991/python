def longestUniqueSubStr(s):
    n = len(s)
    d = {s[0]: 0}
    maxGlobal = 1
    maxLocal = 1
    start = 0
    d = {s[0]: 0}
    for i in range(1, n):
        c = s[i]
        if c not in d:
            maxLocal += 1
        else:
            if d[c] < start:
                maxLocal += 1
            else:
                maxGlobal = max(maxGlobal, maxLocal)
                start = d[c] + 1
                maxLocal = i - start + 1
        d[c] = i
        maxGlobal = max(maxGlobal, maxLocal)
    return maxGlobal


print(longestUniqueSubStr('GEEKSFORGEXS'))
print(longestUniqueSubStr('GEEKSFORGEEKS'))
print(longestUniqueSubStr('ABDEFGABEF'))
print(longestUniqueSubStr('BBBB'))
print(longestUniqueSubStr('BBBBAX'))
