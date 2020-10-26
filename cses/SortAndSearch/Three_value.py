import collections

v = input().split(' ')
n, x = int(v[0]), int(v[1])
arr = [int(c) for c in input().split(' ')]


def f():
    if len(arr) < 3:
        return None
    arr2 = sorted(arr)
    if arr2[-1] + arr2[-2] + arr2[-3] < x:
        return None
    for i, a in enumerate(arr):
        d = {}
        for j, y in enumerate(arr):
            if j == i:
                continue
            if y in d:
                d[y].append(j + 1)
            else:
                d[y] = [j + 1]
        for b in d:
            c = x - (a + b)
            if c in d:
                if c != b:
                    return (i + 1, d[b][0], d[c][0])
                elif c == b and len(d[c]) > 1:
                    return (i + 1, d[b][0], d[b][1])
    return None


ans = f()
if ans:
    print(str(ans[0]) + " " + str(ans[1]) + " " + str(ans[2]))
else:
    print("IMPOSSIBLE")
