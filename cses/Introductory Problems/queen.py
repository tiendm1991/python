def f(result, d, a):
    if len(a) == 8:
        result[0] += 1
        return
    for i in range(8):
        valid = True
        row = len(a)
        if i in d[row]:
            continue
        for j in range(row):
            if a[j] == i:
                valid = False
                break
        if not valid:
            continue
        for j in range(row):
            if i - row == a[j] - j or i + row == a[j] + j:
                valid = False
                break
        if not valid:
            continue
        a.append(i)
        f(result, d, a)
        del a[-1]
    return

n = 8
result = [0]
d = {i : set() for i in range(8)}
for i in range(8):
    s = input()
    for j, c in enumerate(s):
        if c == '*':
            d[i].add(j)
f(result, d, [])
print(result[0])
