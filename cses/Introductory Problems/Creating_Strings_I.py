import collections


def f(n, result, s, str):
    if len(str) == n:
        result.add(str)
        return
    for c in s:
        if s[c] == 0:
            continue
        str += c
        s[c] -= 1
        f(n, result, s, str)
        str = str[:-1]
        s[c] += 1
    return


s = input()
n = len(s)
s = collections.Counter(s)
result = set()
f(n, result, s, '')
result = sorted(result)
print(len(result))
for str in result:
    print(str)
