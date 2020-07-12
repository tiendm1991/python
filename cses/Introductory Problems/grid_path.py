def f(d, result, path, a, cur, step):
    if step == 48:
        result[0] += 1
        return
    if a[step] != '?':
        check = (cur[0] + d[a[step]][0], cur[1] + d[a[step]][1])
        if check not in path:
            path.add(check)
            f(d, result, path, a, check, step+1)
            path.remove(check)
        return
    for next in d:
        check = (cur[0] + d[next][0], cur[1] + d[next][1])
        if 0 <= check[0] < 7 and 0 <= check[1] < 7 and check not in path:
            path.add(check)
            f(d, result, path, a, check, step + 1)
            path.remove(check)
    return


result = [0]
s = input()
a = [c for c in s]
path = {(0, 0)}
d = {'D': (1, 0), 'U': (-1, 0), 'L': (0, -1), 'R': (0, 1)}
f(d, result, path, a, (0, 0), 0)
print(result[0])
