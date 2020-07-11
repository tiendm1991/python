import collections


def f(s):
    n = len(s)
    d = collections.Counter(s)
    oddCount = 0
    for c in d:
        if d[c] % 2 == 1:
            oddCount += 1
    if (n % 2 == 0 and oddCount > 0) or oddCount > 1:
        return "NO SOLUTION"
    center = ""
    left = ""
    for c in d:
        left += c * (d[c] // 2)
        if d[c] % 2 == 1:
            center = c
    return left + center + left[::-1]


s = input()
print(f(s))
